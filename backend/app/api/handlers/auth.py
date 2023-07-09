from uuid import UUID

from fastapi import APIRouter, Response, status

import models
from schemas import token, auth
from api import exceptions
from models.utils.session import get_or_create_session
from security.token.generation import generate_tokens
from security.token.validation import validate_refresh_token

router = APIRouter()


@router.post("/token")
async def token_auth(auth_data: auth.UserAuth) -> token.Tokens:
    db_user = await models.User.filter(email=auth_data.email).first()

    if not db_user or not db_user.check_password(auth_data.password):
        raise exceptions.user.invalid_cred

    session = await get_or_create_session(db_user)

    tokens = await generate_tokens(user=db_user, session=session)

    return tokens


@router.get('/logout/{session_uuid}')
async def logout(session_uuid: UUID) -> Response:
    session = await models.Session.filter(session_id=session_uuid).first()

    if not session:
        return Response(content='You are already logout', status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
    await session.delete()

    return Response(content='success', status_code=status.HTTP_200_OK)


@router.post('/refresh')
async def token_refresh(refresh_token: token.RefreshToken) -> token.AccessToken:
    token_data = await validate_refresh_token(refresh_token)

    session = await models.Session.filter(uuid=token_data.sid).first()
    db_user = await models.User.filter(uuid=UUID(token_data.sub)).first()

    if not (session and db_user):
        raise exceptions.token.invalid_token

    tokens = await generate_tokens(db_user, session)

    return token.AccessToken(access=tokens.access)
