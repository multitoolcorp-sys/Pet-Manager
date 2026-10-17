from typing import List
from fastapi import APIRouter, HTTPException, status, Path
from schemas.mascota import ControlVeterinarioSchema
from core.database import get_mascotas_collection
from utils.mongo import parse_object_id

router = APIRouter()

@router.get(
    "/{id}/controles",
    response_model=List[ControlVeterinarioSchema],
    status_code=status.HTTP_200_OK,
    summary="10. Consultar el historial de controles veterinarios de una mascota",
    description="Retorna el listado completo de controles y atenciones veterinarias registradas para una mascota."
)
async def consultar_historial_controles(
    id: str = Path(..., description="Identificador único (ObjectId) de la mascota")
):
    collection = get_mascotas_collection()
    obj_id = parse_object_id(id)
    doc = await collection.find_one({"_id": obj_id}, {"controles": 1, "nombre": 1})
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mascota con ID '{id}' no encontrada."
        )
    return doc.get("controles", [])

@router.post(
    "/{id}/controles",
    response_model=List[ControlVeterinarioSchema],
    status_code=status.HTTP_201_CREATED,
    summary="10b. Registrar un nuevo control veterinario en el historial",
    description="Agrega un nuevo registro de atención o control al historial de la mascota."
)
async def agregar_control_veterinario(
    id: str = Path(..., description="Identificador único (ObjectId) de la mascota"),
    control: ControlVeterinarioSchema = ...
):
    collection = get_mascotas_collection()
    obj_id = parse_object_id(id)
    control_dict = control.model_dump()
    result = await collection.update_one(
        {"_id": obj_id},
        {"$push": {"controles": control_dict}}
    )
    if result.matched_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Mascota con ID '{id}' no encontrada para registrar el control."
        )
    updated_doc = await collection.find_one({"_id": obj_id}, {"controles": 1})
    return updated_doc.get("controles", [])
