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

    def update(self, username: str, user: UserModel) -> UserResponse:
        """Atualiza um usuário.

        Parameters
        ----------
            username: Identificação do usuário.
            user: Informações do usuário.
        """
        return UserResponse.from_orm(self.repository.update(username, user))

    def delete(self, username: str) -> None:
        """Deleta um usuário.

        Parameters
        ----------
            username: Identificação do usuário.
        """
        self.repository.delete(user=user)

    def find_one(self, username: str) -> UserResponse:
        """Busca um usuário por username.

        Parameters
        ----------
            username: username do usuário.
        """
        return UserResponse.from_orm(self.repository.find_one(username))