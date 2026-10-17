from fastapi import APIRouter, HTTPException, status, Path
from core.database import get_mascotas_collection
from utils.mongo import parse_object_id

router = APIRouter()

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="5. Eliminar una mascota",
    description="Elimina de la base de datos la mascota correspondiente al identificador provisto."
)
async def eliminar_mascota(
    id: str = Path(..., description="Identificador único (ObjectId) de la mascota")
):
    collection = get_mascotas_collection()
    obj_id = parse_object_id(id)
    result = await collection.delete_one({"_id": obj_id})
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mascota con ID '{id}' no encontrada para eliminar."
        )
    return {
        "status": "success",
        "message": "Mascota eliminada correctamente del sistema.",
        "id": id
    }
