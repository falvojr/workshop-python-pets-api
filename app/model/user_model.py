import sqlalchemy as sa

from app.config.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id_ = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String(150), nullable=False, unique=True)
    firstName = sa.Column(sa.String(150), nullable=True)
    lastName = sa.Column(sa.String(150), nullable=True)
    email = sa.Column(sa.String(150), nullable=True)
    password = sa.Column(sa.String(150), nullable=True)
    phone = sa.Column(sa.String(150), nullable=True)
    userStatus = sa.Column(sa.Integer, nullable=True)
