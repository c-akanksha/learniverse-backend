from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

load_dotenv()

username = quote_plus(os.getenv("MONGO_USER"))
password = quote_plus(os.getenv("MONGO_PASSWORD"))

MONGO_URL = f"mongodb+srv://{username}:{password}@cluster0.2plwaee.mongodb.net/learniverse"

client = AsyncIOMotorClient(MONGO_URL)
db = client.get_database("learniverse")