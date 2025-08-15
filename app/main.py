import sys
from pathlib import Path

# Добавляем корень проекта в пути импорта
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from fastapi import FastAPI, Depends, Security, HTTPException, status
from app.core.config import settings
from app.database import engine, Base
from fastapi.security import APIKeyHeader

# Измененный импорт
from app.routers.organizations import router as organizations_router
from app.routers.buildings import router as buildings_router
from app.routers.activities import router as activities_router

app = FastAPI(title="Organization Directory API", docs_url="/docs")

api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )

app.include_router(
    organizations_router,
    prefix="/organizations",
    dependencies=[Depends(verify_api_key)]
)

app.include_router(
    buildings_router,
    prefix="/buildings",
    dependencies=[Depends(verify_api_key)]
)

app.include_router(
    activities_router,
    prefix="/activities",
    dependencies=[Depends(verify_api_key)]
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)