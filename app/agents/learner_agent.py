from app.database.db import db

async def create_learner(data):
    result = await db.learners.insert_one(data)
    return str(result.inserted_id)

async def fetch_learner(email: str):
    existing_user = await db.learners.find_one({"email": email})
    if existing_user:
        return str(existing_user["_id"])
    return ""