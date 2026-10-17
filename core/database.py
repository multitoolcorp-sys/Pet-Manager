from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
from core.config import settings
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class MongoDB:
    client: Optional[AsyncIOMotorClient] = None
    db: Optional[AsyncIOMotorDatabase] = None

db_instance = MongoDB()

async def connect_to_mongo():
    """Conexión a MongoDB Atlas (inicio de la aplicación)."""
    if db_instance.client is None:
        logger.info("Conectando a MongoDB Atlas...")
        db_instance.client = AsyncIOMotorClient(settings.effective_mongo_uri)
        db_instance.db = db_instance.client[settings.effective_db_name]
        logger.info(f"Conexión exitosa a la base de datos: {settings.effective_db_name}")

async def close_mongo_connection():
    """Cierre de conexión con MongoDB."""
    if db_instance.client is not None:
        logger.info("Cerrando conexión con MongoDB...")
        db_instance.client.close()
        db_instance.client = None
        db_instance.db = None
        logger.info("Conexión cerrada.")

def get_database() -> AsyncIOMotorDatabase:
    """Obtiene la base de datos de MongoDB (con inicialización perezosa si es necesario)."""
    if db_instance.db is None or db_instance.client is None:
        db_instance.client = AsyncIOMotorClient(settings.effective_mongo_uri)
        db_instance.db = db_instance.client[settings.effective_db_name]
    return db_instance.db

def get_mascotas_collection() -> AsyncIOMotorCollection:
    """Retorna la colección 'mascotas'."""
    db = get_database()
    return db["mascotas"]
