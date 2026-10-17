from typing import List
from fastapi import APIRouter, Path, status
from schemas.mascota import MascotaResponse
from core.database import get_mascotas_collection
from utils.mongo import serialize_mongo_doc

router = APIRouter()

@router.get(
    "/filtrar/raza/{raza}",
    response_model=List[MascotaResponse],
    status_code=status.HTTP_200_OK,
    summary="8. Filtrar mascotas por raza",
    description="Filtra y retorna todas las mascotas pertenecientes a una raza específica."
)
async def filtrar_mascotas_por_raza(
    raza: str = Path(..., description="Raza de la mascota a filtrar")
):
    collection = get_mascotas_collection()
    cursor = collection.find({"raza": {"$regex": f"^{raza}$", "$options": "i"}})
    mascotas = await cursor.to_list(length=100)
    return [serialize_mongo_doc(doc) for doc in mascotas]
