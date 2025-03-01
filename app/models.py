from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class UserInterests(BaseModel):
    user_id: str
    interests: List[str]

class Accommodation(BaseModel):
    id: str = Field(..., alias="_id")  # On utilise `_id` de MongoDB
    name: str
    localisation: str
    price: int
    description: str
    image: List[str]
    topCriteria: List[str]
    interests: List[str]
    isAvailable: bool
    totalPlaces: int
    numberRoom: int
    squareMeter: int
    bedRoom: int  # Correction du nom de `debRoom` à `bedRoom`
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True
        populate_by_name = True  # Permet d'utiliser `_id` au lieu de `id`
