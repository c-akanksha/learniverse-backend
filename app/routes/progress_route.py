from fastapi import APIRouter
from app.agents.progress_tracker_agent import track_learner_progress
from app.database.db import db

router = APIRouter()


@router.get("/generate/{learner_id}")
async def generate_progress(learner_id: str):

    course = await db.courses.find_one({"learner_id": learner_id})

    if not course:
        return {"success": False, "message": "No course found"}

    modules = course.get("modules", [])
    feedback_data = [
        {
            "module_number": m.get("module_number"),
            "title": m.get("title"),
            "completed": m.get("completed"),
            "quiz": m.get("quiz", {})
        }
        for m in modules
    ]

    analysis = await track_learner_progress(feedback_data)

    return {"success": True, "data": analysis}