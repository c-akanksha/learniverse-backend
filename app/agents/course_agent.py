from app.services.openai_service import client
import json

def generate_course(skill: str, level: str, num_of_modules = 5):
    prompt = f"""
    Generate a course outline for 
    {skill} at {level} level with exactly {num_of_modules}.
    Return ONLY valid JSON in this format:

    {{
      "course_title": "",
      "level": "",
      "total_estimated_time": "",
      "modules": [
        {{
          "module_number": 1,
          "title": "",
          "description": "",
          "reference": "",
          "estimated_time": ""
        }}
      ]
    }}

    Do not return markdown.
    Do not return explanations.
    Return only JSON.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "You are an AI course generator."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    raw_response = response.choices[0].message.content
    return json.loads(raw_response)