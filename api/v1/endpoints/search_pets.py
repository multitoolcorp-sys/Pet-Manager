from typing import List
from fastapi import APIRouter, Query, status
from schemas.mascota import MascotaResponse
from core.database import get_mascotas_collection
from utils.mongo import serialize_mongo_doc

router = APIRouter()

@router.get(
    "/buscar/nombre",
    response_model=List[MascotaResponse],
    status_code=status.HTTP_200_OK,
    summary="6. Buscar mascotas por nombre",
    description="Busca mascotas cuyo nombre coincida de forma parcial o total (búsqueda insensible a mayúsculas)."
)
async def buscar_mascotas_por_nombre(
    nombre: str = Query(..., min_length=1, description="Nombre o fragmento del nombre a buscar")
):
    collection = get_mascotas_collection()
    cursor = collection.find({"nombre": {"$regex": nombre, "$options": "i"}})
    mascotas = await cursor.to_list(length=100)
    return [serialize_mongo_doc(doc) for doc in mascotas]
