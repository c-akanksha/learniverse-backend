from pydantic import BaseModel

class CourseRequest(BaseModel):
    skill: str
    level: str
    num_of_modules: int = 5

class QuestionRequest(BaseModel):
    skill_name: str
    module_title: str

class FeedbackRequest(BaseModel):
    question: str
    answer: str

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

class LearnerRequest(BaseModel):
    learner_id: str