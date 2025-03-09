from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from bson import ObjectId
from app.database import accommodations_collection

def get_recommendations(user_interests):

    interests_text = " ".join(user_interests).lower()
    accommodations = list(accommodations_collection.find({}))

    if not accommodations:
        print("Aucune annonce trouvée dans la base de données !")
        return []

    df = pd.DataFrame(accommodations)

    # Vérifier et transformer ObjectId en string
    if "_id" in df.columns:
        df["_id"] = df["_id"].apply(lambda x: str(x) if isinstance(x, ObjectId) else x)

    # S'assurer que "interests" est une liste
    df["interests"] = df["interests"].apply(lambda x: x if isinstance(x, list) else [])
    df["interests_text"] = df["interests"].apply(lambda x: " ".join(x).lower())

    # Remplacer valeurs NaN par chaîne vide
    df.fillna("", inplace=True)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["interests_text"])
    user_vector = vectorizer.transform([interests_text])

    similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
    df["score"] = similarities

    # Vérifier si au moins une recommandation est pertinente
    if df["score"].max() == 0:
        print("Aucune recommandation pertinente trouvée.")
        return []

    recommendations = df[df["score"] > 0].sort_values("score", ascending=False).head(5).to_dict(orient="records")

    return recommendations
