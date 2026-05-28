from backend.database import players_collection

players = [
    {
        "name": "bruno",
        "password": "123",
        "rank": "Platina",
        "role": "Dano",
        "winrate": 55
    },
    {
        "name": "tankmaster",
        "password": "123",
        "rank": "Platina",
        "role": "Tanque",
        "winrate": 51
    },
    {
        "name": "mercygirl",
        "password": "123",
        "rank": "Platina",
        "role": "Suporte",
        "winrate": 62
    }
]

for player in players:

    existing = players_collection.find_one({
        "name": player["name"]
    })

    if not existing:
        players_collection.insert_one(player)
        print(f'{player["name"]} inserido')

print("Finalizado!")