from fastapi import APIRouter
from api.v1.endpoints import (
    register_pet,
    list_pets,
    get_pet,
    update_pet,
    delete_pet,
    search_pets,
    filter_species,
    filter_breed
)

api_router = APIRouter(prefix="/mascotas", tags=["Mascotas"])

api_router.include_router(register_pet.router)
api_router.include_router(list_pets.router)
api_router.include_router(get_pet.router)
api_router.include_router(update_pet.router)
api_router.include_router(delete_pet.router)
api_router.include_router(search_pets.router)
api_router.include_router(filter_species.router)
api_router.include_router(filter_breed.router)
