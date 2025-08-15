# app/routers/activities.py (пример минимальной версии)
print("Initializing activities router")

from fastapi import APIRouter
router = APIRouter()

print("Activities router created successfully")

@router.get("/test")
def test_endpoint():
    return {"message": "Activities router works"}
