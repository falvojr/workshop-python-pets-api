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
