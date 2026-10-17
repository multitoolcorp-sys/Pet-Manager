from fastapi import APIRouter
from api.v1.endpoints import (
    register_pet
)

api_router = APIRouter(prefix="/mascotas", tags=["Mascotas"])

api_router.include_router(register_pet.router)
