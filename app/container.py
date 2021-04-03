"""Declara os métodos para DI."""
from fastapi import Depends
from sqlalchemy.orm import Session

from app.config.database.connection import get_session
from app.repository import UserRepository


def get_user_repo(session: Session = Depends(get_session)):
    yield UserRepository(session=session)


def get_user_service(user_repository: UserRepository = Depends(get_user_repo)):
    from app.service import UserService

    yield UserService(repository=user_repository)
