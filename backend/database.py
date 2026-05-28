from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

print("URL:", MONGO_URL)

client = MongoClient(MONGO_URL)

db = client["overwatch"]

players_collection = db["players"]

print("Mongo conectado!")