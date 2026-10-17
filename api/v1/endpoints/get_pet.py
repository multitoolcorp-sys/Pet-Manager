from fastapi import APIRouter, HTTPException, status, Path
from schemas.mascota import MascotaResponse
from core.database import get_mascotas_collection
from utils.mongo import serialize_mongo_doc, parse_object_id

router = APIRouter()

@router.get(
    "/{id}",
    response_model=MascotaResponse,
    status_code=status.HTTP_200_OK,
    summary="3. Consultar una mascota mediante su identificador",
    description="Busca y retorna la información completa de una mascota utilizando su ID de MongoDB."
)
async def consultar_mascota_por_id(
    id: str = Path(..., description="Identificador único (ObjectId) de la mascota")
):
    collection = get_mascotas_collection()
    obj_id = parse_object_id(id)
    doc = await collection.find_one({"_id": obj_id})
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mascota con ID '{id}' no encontrada."
        )
    return serialize_mongo_doc(doc)
