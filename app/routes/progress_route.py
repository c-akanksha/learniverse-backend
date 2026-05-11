from fastapi import APIRouter
from app.agents.progress_tracker_agent import ( save_progress, track_learner_progress )
from app.models.base_models import ProgressRequest

router = APIRouter()

@router.post("/save")
async def save_learning_progress(request: ProgressRequest):
    progress_data = request.model_dump()
    inserted_id = await save_progress(progress_data)
    return { "success": True, "inserted_id": inserted_id }

@router.get("/generate/{learner_id}")
async def generate_progress(learner_id: str):
    analysis = await track_learner_progress(learner_id)

    return { "success": True, "data": analysis }