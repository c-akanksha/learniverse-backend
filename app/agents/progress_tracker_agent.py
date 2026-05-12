from app.services.openai_service import client
import json

def calculate_progress(modules):

    total = len(modules)

    completed = sum(1 for m in modules if m.get("completed"))

    scores = [
        m.get("quiz", {}).get("evaluation", {}).get("total_score", 0)
        for m in modules
        if m.get("quiz")
    ]

    avg = sum(scores) / len(scores) if scores else 0

    return {
        "total_modules": total,
        "completed_modules": completed,
        "completion_percentage": round((completed / total) * 100, 2) if total else 0,
        "average_score": round(avg, 2)
    }

async def track_learner_progress(modules: list):
    modules_with_quiz = [
        m for m in modules
        if m.get("quiz")
    ]
    prompt = f"""
    You are Orion — an AI learning intelligence analyst.

    Analyze learner data:

    {json.dumps(modules_with_quiz, indent=2)}

    Generate:

    - learner_summary as string
    - improvement_trends as array of strings
    - strengths as array of strings
    - weak_areas as array of strings
    - motivation_feedback as string
    - next_learning_recommendations as array of strings

    Return ONLY JSON.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "You are Orion — learning intelligence engine. Return ONLY JSON."
            },
            {"role": "user", "content": prompt}
        ]
    )

    ai_result = json.loads(response.choices[0].message.content)
    progress = calculate_progress(modules)

    return {
        "total_modules": progress["total_modules"],
        "completed_modules": progress["completed_modules"],
        "completion_percentage": progress["completion_percentage"],
        "average_score": progress["average_score"],
        "progress_analysis": ai_result
    }