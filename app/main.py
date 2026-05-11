import uvicorn
from fastapi import FastAPI
from app.routes.learning_routes import router as learning_router
from app.routes.quiz_route import router as quiz_router
from app.routes.progress_route import router as progress_router
from app.routes.learner_route import router as learner_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Learniverse AI")

origins = [
    # Local development
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
    # GitHub Pages
    "https://c-akanksha.github.io",
    "https://c-akanksha.github.io/learniverse",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Learniverse is up and running!"}

app.include_router(learning_router, prefix="/api/learning")
app.include_router(quiz_router, prefix="/api/generate")
app.include_router(progress_router, prefix="/api/progress")
app.include_router(learner_router, prefix="/api/learner")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000)