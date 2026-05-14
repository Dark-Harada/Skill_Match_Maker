from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["overwatch"]

players_collection = db["players"]
