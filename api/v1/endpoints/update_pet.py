from fastapi import APIRouter, HTTPException, status, Path
from schemas.mascota import MascotaUpdate, MascotaResponse
from core.database import get_mascotas_collection
from utils.mongo import serialize_mongo_doc, parse_object_id

router = APIRouter()

@router.put(
    "/{id}",
    response_model=MascotaResponse,
    status_code=status.HTTP_200_OK,
    summary="4. Modificar la información de una mascota",
    description="Actualiza la información de una mascota existente identificada por su ID."
)
async def modificar_mascota(
    id: str = Path(..., description="Identificador único (ObjectId) de la mascota"),
    datos: MascotaUpdate = ...
):
    collection = get_mascotas_collection()
    obj_id = parse_object_id(id)
    
    update_data = {k: v for k, v in datos.model_dump().items() if v is not None}
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Debe proporcionar al menos un campo para actualizar."
        )
        
    result = await collection.update_one({"_id": obj_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mascota con ID '{id}' no encontrada para modificar."
        )
        
    updated_doc = await collection.find_one({"_id": obj_id})
    return serialize_mongo_doc(updated_doc)
