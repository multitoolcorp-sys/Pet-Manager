from fastapi import APIRouter, HTTPException, status
from schemas.mascota import MascotaCreate, MascotaResponse
from core.database import get_mascotas_collection
from utils.mongo import serialize_mongo_doc

router = APIRouter()

@router.post(
    "/",
    response_model=MascotaResponse,
    status_code=status.HTTP_201_CREATED,
    summary="1. Registrar una nueva mascota",
    description="Crea un nuevo documento de mascota con datos básicos, controles, vacunas y propietario."
)
async def registrar_mascota(mascota: MascotaCreate):
    collection = get_mascotas_collection()
    mascota_dict = mascota.model_dump()
    result = await collection.insert_one(mascota_dict)
    
    created_doc = await collection.find_one({"_id": result.inserted_id})
    if not created_doc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al recuperar la mascota registrada"
        )
    return serialize_mongo_doc(created_doc)
