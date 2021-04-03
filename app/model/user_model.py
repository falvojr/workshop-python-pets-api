import sqlalchemy as sa

from app.config.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id_ = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(150), nullable=False)
