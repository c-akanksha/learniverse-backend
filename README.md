# 🚀 Learniverse

Welcome to **Learniverse** — your AI-powered personalized learning universe 🌌✨

Learniverse is an **Agentic AI Learning Platform** that dynamically:
- 📚 Generates courses
- ❓ Creates quizzes
- 🧠 Evaluates learner understanding
- 📈 Tracks progress
- 🎯 Provides AI-powered feedback

Built using:
- ⚡ FastAPI
- 🤖 OpenAI
- 🍃 MongoDB
- 🐍 Python

---

# 🌟 Features

## 🧠 Course Generation Agent
Generate personalized learning modules based on:
- skill
- level
- number of modules

---

## ❓ Question & Feedback Agent
After every module:
- generates assessment questions
- evaluates learner answers
- gives AI-powered feedback
- scores learner performance

---

## 📈 Progress Tracker Agent
Tracks:
- completed modules
- quiz scores
- learning patterns
- strengths & weak areas

Provides:
- AI-generated progress analysis
- recommendations
- improvement trends

---

# 🏗️ Architecture

```txt
                ┌────────────────────┐
                │   Course Agent     │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │  Quiz Agent        │
                │  + Feedback Agent  │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │ Progress Tracker   │
                └─────────┬──────────┘
                          ↓
                     MongoDB 🍃
```

---

# ⚙️ Tech Stack

| Tech | Purpose |
|---|---|
| FastAPI | Backend APIs |
| OpenAI | AI agents |
| MongoDB | Learner progress storage |
| Render | Deployment |
| Python | Backend language |

---

# 📦 Installation

## Clone Repo

```bash
git clone <your_repo_url>
cd learniverse-backend
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_openai_key

MONGO_USER=your_mongodb_user

MONGO_PASSWORD=your_mongodb_password
```

---

# ▶️ Run Project

```bash
uvicorn app.main:app --reload
```

---

# 📄 Swagger Docs

```txt
http://127.0.0.1:8000/docs
```

---

# 🧪 API Endpoints

---

# 👤 Create Learner

## Endpoint

```http
POST /api/learner/create
```

## Request

```json
{
    "email": "test@test.com",
    "name": "Test User"
}
```

## Response

```json
{
    "success": true,
    "learner_id": "6a01dfg6b52f2b9f443f"
}
```

---

# 👤 Login

```http
POST /api/learner/login
```

## Request

```json
{
    "email": "test@test.com"
}
```

## Response

```json
{
    "success": true,
    "learner_id": "6a01dfg6b52f2b9f443f"
}
```
---

# 🧠 Generate Course

## Endpoint

```http
POST /api/learning/generate-course
```

## Request

```json
{
  "skill": "React",
  "level": "Beginner",
  "num_of_modules": 5 // 5 by default
}
```

## Response

```json
{
  "success": true,
  "data": {
    "course_title": "React for Beginners",
    "level": "Beginner",
    "total_estimated_time": "10 hours",
    "modules": [
      {
        "module_number": 1,
        "title": "Introduction to React",
        "description": "Learn the basics of React and component-based architecture.",
        "reference": "https://reactjs.org/docs/getting-started.html",
        "estimated_time": "2 hours"
      }
    ]
  }
}
```

---

# ❓ Generate Question

## Endpoint

```http
POST /api/generate/question
```

## Request

```json
{
  "skill_name": "React",
  "module_title": "React Hooks"
}
```

## Response

```json
{
  "success": true,
  "data": {
    "question": "What is JSX?",
    "difficulty": "easy"
  }
}
```

---

# 🧠 Evaluate Learner Answer

## Endpoint

```http
POST /api/generate/feedback
```

## Request

```json
{
  "question": "What is JSX?",
  "expected_answer": "JSX allows writing HTML-like syntax in JavaScript.",
  "user_answer": "It allows us to write HTML in React."
}
```

## Response

```json
{
  "success": true,
  "data": {
    "score": 8,
    "feedback": "Good understanding of JSX.",
    "strengths": ["Understood HTML-like syntax concept."],
    "improvements": ["Could explain JavaScript integration better."],
    "correct": true
  }
}
```

---

# 💾 Save Learner Progress

## Endpoint

```http
POST /api/progress/save
```

## Request

```json
{
  "learner_id": "681f92c0b4d2c34f12345678",
  "skill_name": "React",
  "module_title": "React Hooks",
  "completed": true,
  "score": 8
}
```

## Response

```json
{
  "success": true,
  "inserted_id": "681fa92cb4d2c34f99887766"
}
```

---

# 📈 Generate Progress Analysis

## Endpoint

```http
GET api/progress/generate/{learner_id}
```

## Example

```http
GET api/progress/generate/681f92c0b4d2c34f12345678
```

## Response

```json
{
  "success": true,
  "data": {
    "total_modules": 5,
    "completed_modules": 4,
    "completion_percentage": 80,
    "average_score": 7.5,
    "progress_analysis": {
      "summary": "Learner is improving steadily.",
      "improvement_trend": "Positive",
      "strengths": "The learner demonstrates competency in React Hooks, indicating an ability to understand and apply modern React features effectively.",
      "weak_areas": "Based on the current data, no specific weak areas are identified. Continued assessment across multiple modules is recommended to pinpoint areas needing enhancement.",
      "motivation_feedback": "Excellent consistency!",
      "next_steps": [
        "Practice advanced Hooks concepts."
      ]
    }
  }
}
```

---

# 🌍 Deployment

Backend deployed on:

```txt
Render
```

Frontend planned on:

```txt
Vercel
```

---

# 🚀 Future Improvements

- 🔐 Authentication
- 🧠 Long-term AI Memory
- 🎙️ Voice Learning
- 📊 Dashboard Analytics
- 🧩 Adaptive Difficulty
- 📚 RAG-based Learning
- 🤝 Multi-agent orchestration
- 🧑‍🏫 AI Mentor

---

# 💡 Inspiration

Learniverse was built to explore how **Agentic AI systems** can create adaptive, intelligent, and personalized learning experiences.

---

# 🪐 Welcome to the Learniverse 🌌