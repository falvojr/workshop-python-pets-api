from fastapi import Depends

from app.api.v1.response.user_response import UserResponse
from app.container import get_user_repo
from app.model import UserModel
from app.repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, user: UserModel) -> UserResponse:
        """Insere novo usuário.

        Parameters
        ----------
            user: Informações do usuário.
        """
        user = self.repository.save(user=user)

        return UserResponse.from_orm(user)
