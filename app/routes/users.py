from fastapi import APIRouter, HTTPException
from app.database import users_collection
from app.models import UserInterests

router = APIRouter()

@router.post("/interests/{user_id}")
def save_interests(user_id: str, interests: UserInterests):
    users_collection.update_one(
        {"user_id": user_id},
        {"$set": interests.dict()},
        upsert=True
    )
    return {"message": "Intérêts enregistrés"}

@router.get("/interests/{user_id}")
def get_interests(user_id: str):
    user = users_collection.find_one({"user_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")
    return {"interests": user.get("interests", [])}
