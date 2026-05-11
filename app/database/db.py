from urllib.parse import quote_plus
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

username = quote_plus(MONGO_USER)
password = quote_plus(MONGO_PASSWORD)

MONGO_URL = (
    f"mongodb+srv://{username}:{password}"
    "@cluster0.2plwaee.mongodb.net/learniverse"
    "?retryWrites=true&w=majority&appName=Cluster0"
)

client = AsyncIOMotorClient(MONGO_URL)
db = client.get_default_database()