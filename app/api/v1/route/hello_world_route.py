from fastapi import APIRouter

app = APIRouter(prefix="/api/v1")


@app.get("/hello-world", summary="Exibe mensagem de olá mundo.")
def hello_world(name: str):
    """Exibe mensagem de olá mundo para o usuário."""
    return {"message": f"Hello World {name}!"}
