from fastapi import APIRouter
from app.agents.quiz_agent import generate_feedback, generate_questions
from app.database.db import db
from app.models.base_models import QuestionRequest, FeedbackRequest

router = APIRouter()


@router.post("/question")
async def create_question(request: QuestionRequest):
    course = await db.courses.find_one(
        {"learner_id": request.learner_id}
    )

    updated = []

    for m in course["modules"]:
        if m["title"] == request.module_title:
            m["completed"] = True
        updated.append(m)

    await db.courses.update_one(
        {"learner_id": request.learner_id},
        {"$set": {"modules": updated}}
    )

    return {
        "success": True,
        "data": generate_questions(request.skill_name, request.module_title)
    }


@router.post("/feedback")
async def create_feedback(request: FeedbackRequest):
    qa_pairs = [
        qa.model_dump()
        for qa in request.qa_pairs
    ]
    feedback = generate_feedback(qa_pairs)

    course = await db.courses.find_one(
        {"learner_id": request.learner_id}
    )

    updated = []

    for m in course["modules"]:
        if m["title"] == request.module_title:
            m["quiz"] = {
                "qa_pairs": qa_pairs,
                "evaluation": feedback
            }
        updated.append(m)

    await db.courses.update_one(
        {"learner_id": request.learner_id},
        {"$set": {"modules": updated}}
    )

    return {"success": True, "data": feedback}