from typing import List

from pydantic import BaseModel


class CourseRequest(BaseModel):
    skill: str
    level: str
    learner_id: str
    num_of_modules: int = 5


class QuestionRequest(BaseModel):
    learner_id: str
    course_id: str
    skill_name: str
    module_title: str


class QAPair(BaseModel):
    question: str
    answer: str
    difficulty: str


class FeedbackRequest(BaseModel):
    learner_id: str
    course_id: str
    module_title: str
    qa_pairs: List[QAPair]


class ProgressRequest(BaseModel):
    learner_id: str
    skill_name: str
    module_title: str
    completed: bool
    score: int


class LearnerRequest(BaseModel):
    name: str
    email: str


class LoginRequest(BaseModel):
    email: str
