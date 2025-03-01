from fastapi import FastAPI
from .routes import users, recommendations
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Inclusion des routes
app.include_router(users.router)
app.include_router(recommendations.router)

# Middleware pour autoriser les requêtes CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines (remplace "*" par ["http://localhost:3000"] en prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API de recommandation en ligne 🚀"}
