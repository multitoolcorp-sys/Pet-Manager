from bson import ObjectId
from fastapi import HTTPException, status
from pydantic import BeforeValidator
from typing import Annotated, Optional

# Helper para validación y conversión de ObjectId en esquemas Pydantic
PyObjectId = Annotated[str, BeforeValidator(str)]

def parse_object_id(id_str: str) -> ObjectId:
    """Valida y convierte un string en un ObjectId de MongoDB."""
    if not ObjectId.is_valid(id_str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El identificador '{id_str}' no es un ObjectId válido de MongoDB."
        )
    return ObjectId(id_str)

def serialize_mongo_doc(doc: Optional[dict]) -> Optional[dict]:
    """Convierte el campo _id de MongoDB a un string 'id' serializable."""
    if not doc:
        return None
    data = dict(doc)
    if "_id" in data:
        data["id"] = str(data["_id"])
    return data
