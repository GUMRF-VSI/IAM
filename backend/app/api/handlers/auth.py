from uuid import UUID

from fastapi import APIRouter, Response, status

from api import exceptions
from models import user as user_models, session as session_models
from schemas import token as token_schemas, auth as auth_schemas
from models.utils.session import get_or_create_session
from security.token import generation, validation

router = APIRouter()


@router.post("/token")
async def token_auth(auth_data: auth_schemas.UserAuth) -> token_schemas.Tokens:
    db_user = await user_models.User.filter(email=auth_data.email).first()

    if not db_user or not db_user.check_password(auth_data.password):
        raise exceptions.auth.invalid_cred

    session = await get_or_create_session(db_user)

    tokens = await generation.generate_tokens(user=db_user, session=session)

    return tokens


@router.get('/logout/{session_uuid}')
async def logout(session_uuid: UUID) -> Response:
    session = await session_models.Session.filter(session_id=session_uuid).first()

    if not session:
        return Response(content='You are already logout', status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
    await session.delete()

    return Response(content='success', status_code=status.HTTP_200_OK)


@router.post('/refresh')
async def token_refresh(refresh_token: token_schemas.RefreshToken) -> token_schemas.AccessToken:
    token_data = await validation.validate_refresh_token(refresh_token)

    session = await session_models.Session.filter(uuid=token_data.sid).first()
    db_user = await session.user.first()

    if not (session and db_user):
        raise exceptions.token.invalid_token

    tokens = await generation.generate_tokens(db_user, session)

    return token_schemas.AccessToken(access=tokens.access)
