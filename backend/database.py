from pymongo import MongoClient

# CONEXÃO COM O MONGODB
client = MongoClient("mongodb://localhost:27017")

# BANCO DE DADOS
db = client["overwatch"]

# COLLECTION PLAYERS
players_collection = db["players"]
