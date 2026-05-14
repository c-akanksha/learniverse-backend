# agents/course_agent.py
import json

from app.services.openai_service import client


def generate_course(skill, level, num_modules, learner_state=None):

    prompt = f"""
    You are Astra — an adaptive curriculum designer.

    Skill: {skill}
    Level: {level}
    Modules: {num_modules}

    Learner state:
    {json.dumps(learner_state or {}, indent=2)}

    Generate exactly one external learning resource URL for this module.

Rules:
- The response MUST be a valid HTTPS URL only.
- Do NOT return any explanation, markdown, bullets, or extra text.
- The URL should directly help users learn the topic in a practical and structured way.
- Prefer high-quality educational sources such as:
  - official documentation
  - MDN
  - freeCodeCamp
  - GeeksforGeeks
  - roadmap.sh
  - JavaScript.info
  - React docs
  - Next.js docs
  - TypeScript docs
  - Coursera
  - edX
  - Khan Academy
  - YouTube tutorials from respected educators
- Avoid:
  - Wikipedia
  - random blogs
  - low-quality SEO sites
  - homepages unrelated to the topic
  - broken or inaccessible links
- The link should match the module difficulty level and topic accurately.
- Prefer beginner-friendly resources unless the module is marked advanced.
    
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
            {"role": "user", "content": prompt},
        ],
    )

    return json.loads(res.choices[0].message.content)
