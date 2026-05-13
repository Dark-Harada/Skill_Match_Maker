from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import random

from backend.database import players_collection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="backend/frontend"), name="static")


@app.get("/", response_class=HTMLResponse)
def home():
    with open("backend/frontend/index.html", encoding="utf-8") as f:
        return f.read()


# LISTAR JOGADORES
@app.get("/players")
def get_players():

    players = []

    for player in players_collection.find():

        players.append({
            "id": str(player["_id"]),
            "name": player["name"],
            "rank": player["rank"],
            "winrate": player["winrate"]
        })

    return players


# CRIAR JOGADOR
@app.post("/players")
def create_player(player: dict):

    result = players_collection.insert_one(player)

    return {
        "message": "Player criado com sucesso",
        "id": str(result.inserted_id)
    }


# MATCHMAKING
@app.get("/matchmaking/{player_name}")
def matchmaking(player_name: str):

    user = players_collection.find_one({
        "name": player_name
    })

    if not user:
        return {"error": "Usuário não encontrado"}

    others = list(players_collection.find({
        "name": {"$ne": player_name}
    }))

    if len(others) < 4:
        return {
            "error": "Jogadores insuficientes para criar partida"
        }

    team_random = random.sample(others, 4)

    team = [{
        "name": user["name"],
        "rank": user["rank"],
        "winrate": user["winrate"]
    }]

    for p in team_random:

        team.append({
            "name": p["name"],
            "rank": p["rank"],
            "winrate": p["winrate"]
        })

    return team
