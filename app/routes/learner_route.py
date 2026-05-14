from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.agents.learner_agent import create_learner, fetch_learner
from app.models.base_models import LearnerRequest, LoginRequest

router = APIRouter()


@router.post("/create")
async def add_learner(request: LearnerRequest):
    learner_data = request.model_dump()
    learner_id = await create_learner(learner_data)

    return {"success": True, "learner_id": learner_id}


@router.post("/login")
async def get_learner(request: LoginRequest):
    learner_email = request.email
    learner_id = await fetch_learner(learner_email)
    if not learner_id:
        return JSONResponse(status_code=404, content={"success": False})

    return {"success": True, "learner_id": learner_id}
