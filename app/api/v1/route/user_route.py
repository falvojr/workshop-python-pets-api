from fastapi import APIRouter, Depends, status

from app.api.v1.request.user_request import UserRequest
from app.api.v1.response.user_response import UserResponse
from app.container import get_user_service
from app.service.user_service import UserService

app = APIRouter(prefix="/api/v1")


@app.post(
    "/user",
    response_model=UserResponse,
    response_model_exclude_unset=True,
    status_code=status.HTTP_201_CREATED,
    summary="Cria usuário.",
)
def create_user(user: UserRequest, user_service: UserService = Depends(get_user_service)):
    """Cria novo usuário."""
    return user_service.create(user=user.model)
