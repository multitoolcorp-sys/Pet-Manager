from typing import List
from fastapi import APIRouter, Path, status
from schemas.mascota import MascotaResponse
from core.database import get_mascotas_collection
from utils.mongo import serialize_mongo_doc

router = APIRouter()

@router.get(
    "/filtrar/especie/{especie}",
    response_model=List[MascotaResponse],
    status_code=status.HTTP_200_OK,
    summary="7. Filtrar mascotas por especie",
    description="Filtra y retorna todas las mascotas pertenecientes a una especie determinada (ej. Canino, Felino)."
)
async def filtrar_mascotas_por_especie(
    especie: str = Path(..., description="Especie de la mascota a filtrar")
):
    collection = get_mascotas_collection()
    cursor = collection.find({"especie": {"$regex": f"^{especie}$", "$options": "i"}})
    mascotas = await cursor.to_list(length=100)
    return [serialize_mongo_doc(doc) for doc in mascotas]
