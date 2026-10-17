from typing import List
from fastapi import APIRouter, Query, status
from schemas.mascota import MascotaResponse
from core.database import get_mascotas_collection
from utils.mongo import serialize_mongo_doc

router = APIRouter()

@router.get(
    "/",
    response_model=List[MascotaResponse],
    status_code=status.HTTP_200_OK,
    summary="2. Listar todas las mascotas",
    description="Obtiene el listado completo de mascotas registradas con soporte de paginación."
)
async def listar_mascotas(
    skip: int = Query(default=0, ge=0, description="Número de registros a omitir"),
    limit: int = Query(default=100, ge=1, le=500, description="Cantidad máxima de mascotas a retornar")
):
    collection = get_mascotas_collection()
    cursor = collection.find().skip(skip).limit(limit)
    mascotas = await cursor.to_list(length=limit)
    return [serialize_mongo_doc(doc) for doc in mascotas]
