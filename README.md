# Pet-Manager API 🐾

API REST desarrollada con **FastAPI** y **MongoDB Atlas** para la administración de mascotas registradas en clínicas y centros veterinarios (Proyecto 12).

---

## 🌐 Enlaces de Entrega del Proyecto

- **Repositorio en GitHub:** [https://github.com/multitoolcorp-sys/Pet-Manager.git](https://github.com/multitoolcorp-sys/Pet-Manager.git)
- **Proyecto Funcionando en Vercel (Producción):** [https://pet-manager-livid.vercel.app](https://pet-manager-livid.vercel.app)
- **Documentación Interactiva (Swagger UI en Vercel):** [https://pet-manager-livid.vercel.app/docs](https://pet-manager-livid.vercel.app/docs)

---

## 📁 Estructura del Proyecto

El proyecto cumple exactamente con la arquitectura modular requerida en la especificación:

```text
Pet-Manager/
├── .github/
│   └── .gitkeep
├── api/
│   └── v1/
│       ├── router.py             # Registra y centraliza los routers de endpoints
│       └── endpoints/
│           ├── __init__.py
│           ├── register_pet.py       # 1. Registrar nueva mascota (POST /api/v1/mascotas/)
│           ├── list_pets.py          # 2. Listar todas las mascotas (GET /api/v1/mascotas/)
│           ├── get_pet.py            # 3. Consultar mascota por ID (GET /api/v1/mascotas/{id})
│           ├── update_pet.py         # 4. Modificar información (PUT /api/v1/mascotas/{id})
│           ├── delete_pet.py         # 5. Eliminar mascota (DELETE /api/v1/mascotas/{id})
│           ├── search_pets.py        # 6. Buscar por nombre (GET /api/v1/mascotas/buscar/nombre)
│           ├── filter_species.py     # 7. Filtrar por especie (GET /api/v1/mascotas/filtrar/especie/{especie})
│           ├── filter_breed.py       # 8. Filtrar por raza (GET /api/v1/mascotas/filtrar/raza/{raza})
│           ├── filter_status.py      # 9. Filtrar por estado (GET /api/v1/mascotas/filtrar/estado/{estado})
│           └── veterinary_records.py # 10. Historial de controles (GET /api/v1/mascotas/{id}/controles)
├── core/
│   ├── __init__.py
│   ├── config.py                 # Settings (lee variables de entorno / MongoDB URI)
│   └── database.py               # Conexión asíncrona a MongoDB Atlas (Motor)
├── schemas/
│   ├── __init__.py
│   └── mascota.py                # Modelos Pydantic (Propietario, Controles, Mascota)
├── utils/
│   ├── __init__.py
│   └── mongo.py                  # Validación de ObjectId y serialización
├── .gitignore
├── main.py                       # Punto de entrada de la aplicación FastAPI
├── requirements.txt
└── README.md
```

---

## 🌿 Ramas de Funcionalidades y Pull Requests hacia `[DEV]`

Cada funcionalidad requerida cuenta con su propio archivo en `api/v1/endpoints/` y su propia rama en inglés creada desde `dev`. Todos los Pull Requests apuntan a la rama base de integración **`dev`**:

| # | Funcionalidad | Módulo / Archivo | Rama (en inglés) | Endpoint HTTP |
|---|---|---|---|---|
| **1** | Registrar nueva mascota | `api/v1/endpoints/register_pet.py` | `feature/01-register-pet` | `POST /api/v1/mascotas/` |
| **2** | Listar todas las mascotas | `api/v1/endpoints/list_pets.py` | `feature/02-list-pets` | `GET /api/v1/mascotas/` |
| **3** | Consultar mascota por ID | `api/v1/endpoints/get_pet.py` | `feature/03-get-pet-by-id` | `GET /api/v1/mascotas/{id}` |
| **4** | Modificar información | `api/v1/endpoints/update_pet.py` | `feature/04-update-pet` | `PUT /api/v1/mascotas/{id}` |
| **5** | Eliminar una mascota | `api/v1/endpoints/delete_pet.py` | `feature/05-delete-pet` | `DELETE /api/v1/mascotas/{id}` |
| **6** | Buscar por nombre | `api/v1/endpoints/search_pets.py` | `feature/06-search-pets-by-name` | `GET /api/v1/mascotas/buscar/nombre` |
| **7** | Filtrar por especie | `api/v1/endpoints/filter_species.py` | `feature/07-filter-pets-by-species` | `GET /api/v1/mascotas/filtrar/especie/{especie}` |
| **8** | Filtrar por raza | `api/v1/endpoints/filter_breed.py` | `feature/08-filter-pets-by-breed` | `GET /api/v1/mascotas/filtrar/raza/{raza}` |
| **9** | Filtrar por estado | `api/v1/endpoints/filter_status.py` | `feature/09-filter-pets-by-status` | `GET /api/v1/mascotas/filtrar/estado/{estado}` |
| **10** | Historial de controles | `api/v1/endpoints/veterinary_records.py` | `feature/10-get-veterinary-records` | `GET /api/v1/mascotas/{id}/controles` |

---

## 🚀 Ejecución Local

### 1. Activar entorno virtual e instalar dependencias
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Iniciar servidor local
```powershell
uvicorn main:app --reload --port 8000
```

Acceder a Swagger UI local: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 3. Ejecutar pruebas automatizadas
```powershell
python test_api.py
```
