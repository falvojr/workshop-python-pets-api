from fastapi import APIRouter, Depends, status, HTTPException

from app.api.v1.request.user_request import UserRequest
from app.api.v1.response.user_response import UserResponse
from app.container import get_user_service
from app.service.user_service import UserService

app = APIRouter(prefix="/api/v1", tags=["User Domain"])


@app.post(
    "/user",
    response_model=UserResponse,
    response_model_exclude_unset=True,
    status_code=status.HTTP_201_CREATED,
    summary="Criar usuário.",
)
def create_user(
    user: UserRequest, user_service: UserService = Depends(get_user_service)
):
    """Cria novo usuário."""
    return user_service.create(user=user.model)


@app.put(
    "/user/{username}",
    response_model=UserResponse,
    response_model_exclude_unset=True,
    status_code=status.HTTP_200_OK,
    summary="Atualizar usuário.",
)
def update_user(
    username: str,
    user: UserRequest,
    user_service: UserService = Depends(get_user_service),
):
    """Atualiza um usuário."""
    return user_service.update(username=username, user=user.model)


@app.delete(
    "/user/{username}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deletar usuário.",
)
def delete_user(
    username: str,
    user_service: UserService = Depends(get_user_service),
):
    """Deleta um usuário."""
    return user_service.delete(username=username)


@app.get(
    "/user/{username}",
    response_model=UserResponse,
    response_model_exclude_unset=True,
    status_code=status.HTTP_200_OK,
    summary="Bsucar usuário.",
)
def find_user(username: str, user_service: UserService = Depends(get_user_service)):
    """Buscar um usuário."""
    return user_service.find_one(username=username)
