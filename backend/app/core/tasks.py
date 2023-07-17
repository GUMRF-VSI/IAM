import logging

from datetime import datetime, timedelta

from core.scheduler import scheduler

from core.settings import settings
from models.session import Session

logger = logging.getLogger(__name__)


@scheduler.task(name="remove_outdated_session")
async def remove_outdated_session():
    exp_session = (datetime.now() - timedelta(settings.SECURITY.REFRESH_TOKEN_EXPIRE))
    sessions = await Session.filter(created_at__gt=exp_session).all()
    for session in sessions:
        await session.delete()
