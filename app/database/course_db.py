from bson import ObjectId

from app.database.db import db
from app.utils.serializer import serialize_doc


async def save_course(course_data):
    result = await db.courses.insert_one(course_data)
    course_data["_id"] = str(result.inserted_id)
    return course_data


async def get_course(learner_id, course_id):
    course = await db.courses.find_one(
        {"_id": ObjectId(course_id), "learner_id": learner_id}
    )
    if not course:
        return {}
    return serialize_doc(course)
