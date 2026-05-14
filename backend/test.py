from database import players_collection

players = [

    # BRONZE
    {"login": "bronzewolf", "password": "123456", "name": "BronzeWolf", "rank": "Bronze", "winrate": 41, "role": "Dano"},
    {"login": "rustaim", "password": "123456", "name": "RustAim", "rank": "Bronze", "winrate": 39, "role": "Dano"},
    {"login": "noscopebr", "password": "123456", "name": "NoScopeBR", "rank": "Bronze", "winrate": 43, "role": "Dano"},
    {"login": "slowtank", "password": "123456", "name": "SlowTank", "rank": "Bronze", "winrate": 40, "role": "Tanque"},
    {"login": "babydva", "password": "123456", "name": "BabyDva", "rank": "Bronze", "winrate": 42, "role": "Tanque"},

    # PRATA
    {"login": "silvershot", "password": "123456", "name": "SilverShot", "rank": "Prata", "winrate": 48, "role": "Dano"},
    {"login": "healfast", "password": "123456", "name": "HealFast", "rank": "Prata", "winrate": 47, "role": "Suporte"},
    {"login": "moonarrow", "password": "123456", "name": "MoonArrow", "rank": "Prata", "winrate": 49, "role": "Dano"},
    {"login": "quickmercy", "password": "123456", "name": "QuickMercy", "rank": "Prata", "winrate": 46, "role": "Suporte"},
    {"login": "shieldking", "password": "123456", "name": "ShieldKing", "rank": "Prata", "winrate": 50, "role": "Tanque"},

    # OURO
    {"login": "goldenaim", "password": "123456", "name": "GoldenAim", "rank": "Ouro", "winrate": 54, "role": "Dano"},
    {"login": "belinha", "password": "123456", "name": "Belinha", "rank": "Ouro", "winrate": 57, "role": "Suporte"},
    {"login": "lunafps", "password": "123456", "name": "LunaFPS", "rank": "Ouro", "winrate": 53, "role": "Dano"},
    {"login": "rushzarya", "password": "123456", "name": "RushZarya", "rank": "Ouro", "winrate": 55, "role": "Tanque"},
    {"login": "firewidow", "password": "123456", "name": "FireWidow", "rank": "Ouro", "winrate": 56, "role": "Dano"},

    # PLATINA
    {"login": "melissa", "password": "123456", "name": "Melissa", "rank": "Platina", "winrate": 58, "role": "Suporte"},
    {"login": "ghostaim", "password": "123456", "name": "GhostAim", "rank": "Platina", "winrate": 59, "role": "Dano"},
    {"login": "icesupport", "password": "123456", "name": "IceSupport", "rank": "Platina", "winrate": 60, "role": "Suporte"},
    {"login": "stormtracer", "password": "123456", "name": "StormTracer", "rank": "Platina", "winrate": 61, "role": "Dano"},
    {"login": "pulsereaper", "password": "123456", "name": "PulseReaper", "rank": "Platina", "winrate": 57, "role": "Tanque"},

    # DIAMANTE
    {"login": "shadowx", "password": "123456", "name": "ShadowX", "rank": "Diamante", "winrate": 62, "role": "Dano"},
    {"login": "tirocerto", "password": "123456", "name": "TiroCerto", "rank": "Diamante", "winrate": 64, "role": "Dano"},
    {"login": "dragonaim", "password": "123456", "name": "DragonAim", "rank": "Diamante", "winrate": 63, "role": "Dano"},
    {"login": "nanoboost", "password": "123456", "name": "NanoBoost", "rank": "Diamante", "winrate": 65, "role": "Suporte"},
    {"login": "skyblade", "password": "123456", "name": "SkyBlade", "rank": "Diamante", "winrate": 66, "role": "Suporte"},

    # MESTRE
    {"login": "mastermind", "password": "123456", "name": "MasterMind", "rank": "Mestre", "winrate": 71, "role": "Tanque"},
    {"login": "zencore", "password": "123456", "name": "ZenCore", "rank": "Mestre", "winrate": 72, "role": "Suporte"},
    {"login": "headhunter", "password": "123456", "name": "HeadHunter", "rank": "Mestre", "winrate": 73, "role": "Dano"},
    {"login": "blinkqueen", "password": "123456", "name": "BlinkQueen", "rank": "Mestre", "winrate": 74, "role": "Dano"},
    {"login": "ultramercy", "password": "123456", "name": "UltraMercy", "rank": "Mestre", "winrate": 70, "role": "Suporte"},

    # GRÃO-MESTRE
    {"login": "gmshadow", "password": "123456", "name": "GMShadow", "rank": "Grão-Mestre", "winrate": 81, "role": "Dano"},
    {"login": "aimgod", "password": "123456", "name": "AimGod", "rank": "Grão-Mestre", "winrate": 83, "role": "Dano"},
    {"login": "voidsniper", "password": "123456", "name": "VoidSniper", "rank": "Grão-Mestre", "winrate": 84, "role": "Dano"},
    {"login": "luciofly", "password": "123456", "name": "LucioFly", "rank": "Grão-Mestre", "winrate": 82, "role": "Suporte"},
    {"login": "rapidpulse", "password": "123456", "name": "RapidPulse", "rank": "Grão-Mestre", "winrate": 85, "role": "Tanque"},

]

players_collection.insert_many(players)

print("Jogadores inseridos com sucesso!")