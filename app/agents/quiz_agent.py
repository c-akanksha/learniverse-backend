from app.services.openai_service import client
import json

def generate_questions(skill_name: str, module_title: str):

    prompt = f"""
    You are Quill — expert AI tutor.

    Generate 2 questions for:

    Skill: {skill_name}
    Module: {module_title}

    Requirements:
    - 1 easy question
    - 1 hard question
    - Must test understanding deeply

    Return ONLY JSON:

    {{
      "questions": [
        {{
          "difficulty": "easy",
          "question": ""
        }},
        {{
          "difficulty": "hard",
          "question": ""
        }}
      ]
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are Quill — quiz generator."},
            {"role": "user", "content": prompt}
        ]
    )

    return json.loads(response.choices[0].message.content)

def generate_feedback(qa_pairs: list):

    prompt = f"""
    You are Quill — strict AI evaluator.

    Evaluate ALL answers together and give unified feedback.

    Data:
    {json.dumps(qa_pairs, indent=2)}

    Each item contains:
    - question
    - answer
    - difficulty

    Return ONLY JSON:

    {{
      "total_score": 0,
      "correctness_summary": "",
      "strengths": [],
      "improvements": [],
      "conceptual_gaps": [],
      "final_feedback": "",
      "correct": true
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are Quill — evaluation engine."},
            {"role": "user", "content": prompt}
        ]
    )

    return json.loads(response.choices[0].message.content)