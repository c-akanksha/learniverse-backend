from fastapi import APIRouter
from app.agents.quiz_agent import ( generate_question, generate_feedback )
from app.models.base_models import QuestionRequest, FeedbackRequest

router = APIRouter();

@router.post("/question")
def create_question(request: QuestionRequest):
    question = generate_question(request.skill_name, request.module_title)
    return { "success": True, "data": question }

@router.post("/feedback")
def create_feedback(request: FeedbackRequest):
    feedback = generate_feedback(request.question, request.answer)
    return { "success": True, "data": feedback }

