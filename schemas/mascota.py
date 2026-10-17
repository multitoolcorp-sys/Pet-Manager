from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from utils.mongo import PyObjectId

class PropietarioSchema(BaseModel):
    nombre: str = Field(..., min_length=2, description="Nombre completo del propietario")
    telefono: str = Field(..., min_length=7, description="Teléfono de contacto")
    email: EmailStr = Field(..., description="Correo electrónico del propietario")

    model_config = {
        "json_schema_extra": {
            "example": {
                "nombre": "Carlos Gómez",
                "telefono": "+56912345678",
                "email": "carlos.gomez@example.com"
            }
        }
    }

class ControlVeterinarioSchema(BaseModel):
    fecha: str = Field(
        default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%d"),
        description="Fecha del control (YYYY-MM-DD)"
    )
    motivo: str = Field(..., description="Motivo de la atención o consulta")
    diagnostico: Optional[str] = Field(default="En evaluación", description="Diagnóstico del veterinario")
    tratamiento: Optional[str] = Field(default="Ninguno", description="Tratamiento prescrito")
    veterinario: Optional[str] = Field(default="Veterinario de turno", description="Nombre del profesional")

    model_config = {
        "json_schema_extra": {
            "example": {
                "fecha": "2026-10-16",
                "motivo": "Control anual de rutina",
                "diagnostico": "Estado de salud óptimo",
                "tratamiento": "Desparasitación interna",
                "veterinario": "Dra. Laura Méndez"
            }
        }
    }

class MascotaBase(BaseModel):
    nombre: str = Field(..., min_length=1, description="Nombre de la mascota")
    especie: str = Field(..., description="Especie (Canino, Felino, etc.)")
    raza: str = Field(..., description="Raza de la mascota")
    edad: int = Field(..., ge=0, description="Edad en años")
    sexo: str = Field(..., description="Sexo (Macho / Hembra)")
    peso: float = Field(..., gt=0, description="Peso en kilogramos")
    estado: str = Field(..., description="Estado (Activo, En tratamiento, Alta, etc.)")
    vacunas: List[str] = Field(default_factory=list, description="Lista de vacunas aplicadas")
    controles: List[ControlVeterinarioSchema] = Field(default_factory=list, description="Historial de controles veterinarios")
    propietario: PropietarioSchema = Field(..., description="Datos del propietario")

class MascotaCreate(MascotaBase):
    model_config = {
        "json_schema_extra": {
            "example": {
                "nombre": "Max",
                "especie": "Canino",
                "raza": "Golden Retriever",
                "edad": 3,
                "sexo": "Macho",
                "peso": 31.5,
                "estado": "Activo",
                "vacunas": ["Rabia", "Polivalente"],
                "controles": [
                    {
                        "fecha": "2026-10-16",
                        "motivo": "Revisión general",
                        "diagnostico": "Saludable",
                        "tratamiento": "Ninguno",
                        "veterinario": "Dr. Fernando Ruiz"
                    }
                ],
                "propietario": {
                    "nombre": "Carlos Gómez",
                    "telefono": "+56912345678",
                    "email": "carlos.gomez@example.com"
                }
            }
        }
    }

class MascotaUpdate(BaseModel):
    nombre: Optional[str] = None
    especie: Optional[str] = None
    raza: Optional[str] = None
    edad: Optional[int] = Field(default=None, ge=0)
    sexo: Optional[str] = None
    peso: Optional[float] = Field(default=None, gt=0)
    estado: Optional[str] = None
    vacunas: Optional[List[str]] = None
    controles: Optional[List[ControlVeterinarioSchema]] = None
    propietario: Optional[PropietarioSchema] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "peso": 32.0,
                "estado": "En tratamiento"
            }
        }
    }

class MascotaResponse(MascotaBase):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True
    }
