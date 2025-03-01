from fastapi import APIRouter, HTTPException
from app.database import users_collection
from app.services.recommendation import get_recommendations

router = APIRouter()

@router.get("/recommend/{user_id}")
def recommend(user_id: str):
    user = users_collection.find_one({"user_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    recommendations = get_recommendations(user["interests"])
    return {"recommendations": recommendations}
