from fastapi import FastAPI, status
from sqlalchemy.orm.exc import NoResultFound
from starlette.responses import JSONResponse
from starlette.requests import Request

from app.api.v1 import hello_world_app, user_app
from app.config.database import Base, engine

app = FastAPI()


@app.on_event("startup")
def startup_event():
    """Inicializa banco de dados."""
    from app import model  # noqa

    Base.metadata.create_all(bind=engine)


@app.exception_handler(NoResultFound)
def no_result_handler(request: Request, exc: NoResultFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"mensagem": f"Recurso não encontrado: {str(exc)}."},
    )


@app.exception_handler(Exception)
def generic_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"mensagem": f"Ocorreu um erro inesperado: {str(exc)}."},
    )


app.include_router(hello_world_app)
app.include_router(user_app)
