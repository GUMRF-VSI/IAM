from datetime import datetime

from models.session import Session
from models.user import User


async def get_or_create_session(user: User) -> Session:
    session = await Session.filter(user_id=user.id).first()
    if not session:
        session = await Session.create(user_id=user.id)
    fields_to_update = dict(created_at=datetime.now())
    await session.update_from_dict(fields_to_update)
    return session


async def validate_session(session_id) -> Session:
    session = await Session.filter(session_id=session_id).first()
    return session

