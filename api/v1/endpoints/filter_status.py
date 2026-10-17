from typing import List
from fastapi import APIRouter, Path, status
from schemas.mascota import MascotaResponse
from core.database import get_mascotas_collection
from utils.mongo import serialize_mongo_doc

router = APIRouter()

@router.get(
    "/filtrar/estado/{estado}",
    response_model=List[MascotaResponse],
    status_code=status.HTTP_200_OK,
    summary="9. Filtrar mascotas por estado",
    description="Filtra y retorna todas las mascotas con un estado específico (ej. Activo, En tratamiento, Alta)."
)
async def filtrar_mascotas_por_estado(
    estado: str = Path(..., description="Estado de la mascota a filtrar")
):
    collection = get_mascotas_collection()
    cursor = collection.find({"estado": {"$regex": f"^{estado}$", "$options": "i"}})
    mascotas = await cursor.to_list(length=100)
    return [serialize_mongo_doc(doc) for doc in mascotas]
