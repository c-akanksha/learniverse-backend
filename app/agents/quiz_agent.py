from app.services.openai_service import client
import json

def generate_question(skill_name: str, module_title: str):
    prompt = f"""
    Generate 1 learning assessment question that must
    be asked after a person completes learning of the 
    {module_title} module of {skill_name} skill.
    Return JSON in this format:
    {{
        "question": "",
        "difficulty": ""
    }} 
    """
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI quiz generator"
                    "Return valid JSON only"
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    raw_responses = response.choices[0].message.content
    return json.loads(raw_responses)

def generate_feedback(question: str, answer: str):
    prompt = f"""
    Evaluate the learner's answer - {answer} to the question - {question}
    Return JSON in this format:

    {{
      "score": 0,
      "feedback": "",
      "strengths": [],
      "improvements": [],
      "correct": true
    }}
    Score should be between 0 and 10.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "You are an expert AI tutor"
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    raw_response = response.choices[0].message.content
    return json.loads(raw_response)