from fastapi import FastAPI

from app.api.v1 import hello_world_app, user_app
from app.config.database import Base, engine

app = FastAPI()


@app.on_event("startup")
def startup_event():
    """Inicializa banco de dados."""
    from app import model  # noqa

    Base.metadata.create_all(bind=engine)


app.include_router(hello_world_app)
app.include_router(user_app)
