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


# 🔥 LOGIN
@app.post("/login")
def login(data: dict):

    user = players_collection.find_one({
        "name": data["name"],
        "password": data["password"]
    })

    if not user:
        return {"error": "Login inválido"}

    return {"message": "Login sucesso"}


@app.post("/players")
def create_player(player: dict):

    players_collection.insert_one(player)

    return {"message": "Player criado"}


@app.get("/matchmaking/{player_name}")
def matchmaking(player_name: str):

    user = players_collection.find_one({"name": player_name})

    if not user:
        return {"error": "Usuário não encontrado"}

    rank_order = ["Bronze", "Prata", "Ouro", "Platina", "Diamante", "Mestre", "Grão-Mestre"]

    user_rank_index = rank_order.index(user["rank"])


    def buscar_por_role(role, quantidade):

        encontrados = []

        offsets = [0, 1, -1, 2, -2, 3, -3]

        for offset in offsets:

            idx = user_rank_index + offset

            if idx < 0 or idx >= len(rank_order):
                continue

            rank_alvo = rank_order[idx]

            players = list(players_collection.find({
                "name": {"$ne": player_name},
                "role": role,
                "rank": rank_alvo
            }))

            random.shuffle(players)

            for p in players:
                if len(encontrados) < quantidade:
                    encontrados.append(p)

        return encontrados[:quantidade]


    team = []

    team.append({
        "name": user["name"],
        "rank": user["rank"],
        "winrate": user["winrate"],
        "role": user["role"]
    })


    roles_needed = {
        "Tanque": 1,
        "Dano": 2,
        "Suporte": 2
    }


    roles_needed[user["role"]] -= 1


    for role, qtd in roles_needed.items():

        encontrados = buscar_por_role(role, qtd)

        for p in encontrados:
            team.append({
                "name": p["name"],
                "rank": p["rank"],
                "winrate": p["winrate"],
                "role": p["role"]
            })

    return team