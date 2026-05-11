from fastapi import APIRouter
from app.agents.course_agent import generate_course
from app.models.base_models import CourseRequest

router = APIRouter()

@router.post("/generate-course")
def create_course(request: CourseRequest):
    course = generate_course(request.skill, request.level, request.num_of_modules)
    return { "success": True, "data": course}
