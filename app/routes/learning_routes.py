from fastapi import APIRouter

from app.agents.course_agent import generate_course
from app.database.course_db import get_course, save_course
from app.database.db import db
from app.models.base_models import CourseRequest

router = APIRouter()


@router.post("/generate-course")
async def create_course(request: CourseRequest):

    # CHECK IF COURSE ALREADY EXISTS
    existing_course = await db.courses.find_one(
        {
            "learner_id": request.learner_id,
            "course_title": request.skill,
            "level": request.level,
        }
    )

    # RETURN EXISTING COURSE
    if existing_course:
        existing_course["_id"] = str(existing_course["_id"])

        return {
            "success": True,
            "message": "Course already exists",
            "data": existing_course,
        }

    # GENERATE NEW COURSE
    course = generate_course(request.skill, request.level, request.num_of_modules)

    course["learner_id"] = request.learner_id

    saved = await save_course(course)

    return {"success": True, "data": saved}


@router.get("/{learner_id}/{course_id}")
async def fetch_course(learner_id: str, course_id: str):

    course = await get_course(learner_id, course_id)

    if not course:
        return {"success": False, "message": "No course found"}

    return {"success": True, "data": course}


@router.get("/{learner_id}")
async def get_courses(learner_id: str):

    courses = await db.courses.find({"learner_id": learner_id}).to_list(length=None)

    formatted_courses = []

    for course in courses:
        modules = course.get("modules", [])

        total_modules = len(modules)

        completed_modules = len([m for m in modules if m.get("quiz")])

        formatted_courses.append(
            {
                "_id": str(course["_id"]),
                "course_title": course.get("course_title"),
                "level": course.get("level"),
                "total_modules": total_modules,
                "completed_modules": completed_modules,
            }
        )

    return {"success": True, "data": formatted_courses}
