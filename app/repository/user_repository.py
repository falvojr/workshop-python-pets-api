from typing import Optional
from sqlalchemy.orm.session import Session

from app.model import UserModel


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, user: UserModel) -> UserModel:
        """Cria usuário se não existir, caso contrário atualiza.

        Parameters
        ----------
            user: Informações do usuário.
        """
        with self.session.transaction:
            self.session.merge(user)
            self.session.flush()

        return user

    def update(self, username: str, user: UserModel) -> UserModel:
        """Atualiza um usuário pelo username.

        Parameters
        ----------
            username: username (identificador) do usuário.
            user: Informações do usuário.
        """
        user_db = self.find_one(username)
        user.id_ = user_db.id_
        with self.session.transaction:
            self.session.merge(user)
            self.session.flush()

        return user

    def delete(self, username: str):
        """Deleta um usuário.

        Parameters
        ----------
            username: username (identificador) do usuário.
        """
        user_db = self.find_one(username)
        with self.session.transaction:
            self.session.delete(user_db)
            self.session.flush()

    def find_one(self, username: str) -> Optional[UserModel]:
        """Busca um usuário pelo username.

        Parameters
        ----------
            username: username (identificador) do usuário.
        """
        return self.session.query(UserModel).filter_by(username=username).one()
