from fastapi import APIRouter
from app.agents.course_agent import generate_course
from app.database.course_db import save_course, get_course
from app.models.base_models import CourseRequest

router = APIRouter()


@router.post("/generate-course")
async def create_course(request: CourseRequest):

    course = generate_course(
        request.skill,
        request.level,
        request.num_of_modules
    )

    course["learner_id"] = request.learner_id

    saved = await save_course(course)

    return {"success": True, "data": saved}


@router.get("/{learner_id}")
async def fetch_course(learner_id: str):

    course = await get_course(learner_id)

    if not course:
        return {"success": False, "message": "No course found"}

    return {"success": True, "data": course}