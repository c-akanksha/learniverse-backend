# agents/course_agent.py
from app.services.openai_service import client
import json

def generate_course(skill, level, num_modules, learner_state=None):

    prompt = f"""
    You are Astra — an adaptive curriculum designer.

    Skill: {skill}
    Level: {level}
    Modules: {num_modules}

    Learner state:
    {json.dumps(learner_state or {}, indent=2)}

    RULES FOR REFERENCE:
    - Return relevant URL always.
    
    Return ONLY JSON:
    {{
      "course_title": "",
      "level": "",
      "modules": [
        {{
          "module_number": 1,
          "title": "",
          "description": "",
          "reference": "",
          "estimated_time": "",
          "completed": false
        }}
      ]
    }}
    """

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are Astra — adaptive course designer."},
            {"role": "user", "content": prompt}
        ]
    )

    return json.loads(res.choices[0].message.content)