from app.database.db import db
from app.services.openai_service import client
import json

async def save_progress(data):
    result = await db.progress.insert_one(data)
    return str(result.inserted_id)

async def get_learner_progress(learner_id):
    progress = await db.progress.find({"learner_id": learner_id}).to_list(length = 100)
    for item in progress:
        item["_id"] = str(item["_id"])

    return progress

async def track_learner_progress(learner_id):
    progress = await get_learner_progress(learner_id)

    if not progress:
        return {
            "is_new_learner": True,
            "message": "No learning activity yet.",
            "recommendations": "Start your first course"
        }

    total_modules = len(progress)

    completed_modules = len([
        p for p in progress
        if p.get("complted")
    ])

    average_score = sum(
        p.get("score", 0)
        for p in progress
    ) / total_modules

    prompt = f"""
        Analyze learner progress.
        
        Progress Data: {progress}
        
        Generate:
        - learner summary
        - improvement trends
        - strengths
        - weak areas
        - motivation feedback
        - next learning recommendations
        
        Return JSON format:
        
        {{
            "summary": "",
            "improvement_trends": "",
            "strengths": "",
            "weak_areas": "",
            "motivation_feedback": "",
            "next_steps": []
        }}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "You are an AI progress tracking coach",
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    raw_response = json.loads(response.choices[0].message.content)

    return {
        "is_new_learner": "False",
        "total_modules": total_modules,
        "completed_modules": completed_modules,
        "completion_percentage": round((completed_modules/total_modules)*100, 2),
        "average_score": round(average_score, 2),
        "progress_analysis": raw_response
    }