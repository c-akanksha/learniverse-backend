# 🚀 Learniverse

Welcome to **Learniverse** — an AI-powered adaptive learning universe 🌌✨

Learniverse is a multi-agent AI learning platform that:
- 📚 Generates personalized courses
- ❓ Creates multi-level quizzes
- 🧠 Evaluates learner understanding
- 📈 Tracks learning progress
- 🎯 Provides AI-powered feedback & recommendations

Built using:
- ⚡ FastAPI
- 🤖 OpenAI
- 🍃 MongoDB
- 🐍 Python

---

# 🌟 AI Agents

| Agent | Role | Personality |
|---|---|---|
| **Astra** ✨ | Course Generation Agent | Creative learning architect |
| **Quill** 🪶 | Quiz + Feedback Agent | Friendly but strict AI tutor |
| **Orion** 🌌 | Progress Tracking Agent | Motivational learning analyst |

---

# 🧠 What Learniverse Does

Learniverse creates a personalized AI learning flow:

```txt
User Login/Register
        ↓
Astra generates personalized course
        ↓
User completes module
        ↓
Quill generates quiz (easy + hard)
        ↓
User answers quiz
        ↓
Quill evaluates all answers together
        ↓
Feedback gets saved
        ↓
Orion analyzes overall learner progress
```

---

# 🏗️ Architecture

```txt
                ┌────────────────────┐
                │  Astra ✨          │
                │ Course Generator   │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │  Quill 🪶          │
                │ Quiz + Feedback    │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │  Orion 🌌          │
                │ Progress Analyst   │
                └─────────┬──────────┘
                          ↓
                     MongoDB 🍃
```

---

# ⚙️ Tech Stack

| Tech | Purpose |
|---|---|
| FastAPI | Backend APIs |
| OpenAI API | AI agents |
| MongoDB | Course & learner storage |
| Motor | Async MongoDB driver |
| Python | Backend language |
| Render | Deployment |

---

# 📦 Installation

## Clone Repo

```bash
git clone https://github.com/c-akanksha/learniverse-backend.git
cd learniverse-backend
```

---

# 📥 Install Dependencies

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
  "name": "Akanksha",
  "email": "test@test.com"
}
```

## Response

```json
{
  "success": true,
  "learner_id": "681f92c0b4d2c34f12345678"
}
```

---

# 👤 Login Learner

## Endpoint

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
  "learner_id": "681f92c0b4d2c34f12345678"
}
```

---

# 📚 Generate Course

Astra creates personalized learning modules.

## Endpoint

```http
POST /api/learning/generate-course
```

## Request

```json
{
  "skill": "React",
  "level": "Beginner",
  "learner_id": "681f92c0b4d2c34f12345678",
  "num_of_modules": 5
}
```

## Response

```json
{
  "success": true,
  "data": {
    "course_title": "React for Beginners",
    "level": "Beginner",
    "modules": [
      {
        "module_number": 1,
        "title": "Introduction to ReactJS",
        "description": "Learn React fundamentals.",
        "reference": "https://reactjs.org",
        "estimated_time": "2 hours",
        "completed": false
      }
    ]
  }
}
```

---

# ❓ Generate Quiz

Quill generates:
- 1 easy question
- 1 hard question

## Endpoint

```http
POST /api/generate/question
```

## Request

```json
{
  "learner_id": "681f92c0b4d2c34f12345678",
  "course_id": "1234565",
  "skill_name": "React",
  "module_title": "Introduction to ReactJS"
}
```

## Response

```json
{
  "success": true,
  "data": {
    "questions": [
      {
        "difficulty": "easy",
        "question": "What is JSX?"
      },
      {
        "difficulty": "hard",
        "question": "Explain how React reconciliation works."
      }
    ]
  }
}
```

---

# 🧠 Generate Feedback

Quill evaluates ALL answers together.

## Endpoint

```http
POST /api/generate/feedback
```

## Request

```json
{
  "learner_id": "681f92c0b4d2c34f12345678",
  "course_id": "1234565",
  "module_title": "Introduction to ReactJS",
  "qa_pairs": [
    {
      "question": "What is JSX?",
      "answer": "JSX lets us write HTML-like syntax in React.",
      "difficulty": "easy"
    },
    {
      "question": "Explain virtual DOM.",
      "answer": "Virtual DOM compares differences before updating UI.",
      "difficulty": "hard"
    }
  ]
}
```

## Response

```json
{
  "success": true,
  "data": {
    "total_score": 8,
    "correctness_summary": "Strong foundational understanding.",
    "strengths": [
      "Good understanding of JSX"
    ],
    "improvements": [
      "Could explain reconciliation better"
    ],
    "conceptual_gaps": [
      "Diffing algorithm"
    ],
    "final_feedback": "Great progress overall!",
    "correct": true
  }
}
```

---

# 📈 Generate Progress Analysis

Orion analyzes:
- learning behavior
- strengths
- weak areas
- trends
- next learning recommendations

## Endpoint

```http
GET /api/progress/generate/{learner_id}/{course_id}
```

## Response

```json
{
  "success": true,
  "data": {
    "total_modules": 5,
    "completed_modules": 3,
    "completion_percentage": 60,
    "average_score": 7.5,
    "progress_analysis": {
      "learner_summary": "Learner shows steady growth.",
      "improvement_trends": ["Positive"],
      "strengths": [
        "Strong React fundamentals"
      ],
      "weak_areas": [
        "Advanced React lifecycle concepts"
      ],
      "motivation_feedback": "Excellent consistency!",
      "next_learning_recommendations": [
        "Practice advanced Hooks"
      ]
    }
  }
}
```

---

# 🧠 Fetch All Courses

Fetches all courses belonging to a learner.

## Endpoint

```http
POST /api/learning/{learner_id}
```
## Response

```json
{ 
  "success": true, 
  "data": [ 
    { "_id": "course_id_1", 
      "course_title": "ReactJS Fundamentals", 
      "level": "Beginner", 
      "completed_modules": 1,
      "total_modules": 5
    }, 
    { 
      "_id": "course_id_2", 
      "course_title": "Python Basics", 
      "level": "Intermediate", 
      "completed_modules": 2,
      "total_modules": 7
    } 
  ]
}
```

---

# 💾 MongoDB Stores

- Learners
- Courses
- Modules
- Quiz questions
- Answers
- AI feedback
- Learning analytics

---

# 🌍 Deployment

Backend:
```txt
Render
```

Frontend:
```txt
gh-pages
```

---

# 🚀 Future Improvements

- 🔐 JWT Authentication
- 🧠 Long-term AI memory
- 💬 AI Tutor Chat
- 🎙️ Voice learning
- 📊 Dashboard analytics
- 🧩 Adaptive learning paths
- 📚 RAG-based contextual learning
- 🤝 Multi-agent orchestration
- 🎮 Gamification

---

# 👩‍💻 Developed By

**Akanksha Chandrashekar**

LinkedIn:  
https://linkedin.com/in/c-akanksha

---

# 🪐 Welcome to the Learniverse 🌌