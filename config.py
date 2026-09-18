import os
# -*- coding: utf-8 -*-

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = 6637536360
ADMIN_USERNAME = "onlyworks_11"

CARD_NUMBER = "1250 3000 3707 5266"
CARD_HOLDER = ""

CURRENCY = "сом"

CATALOG = {
    "brawl_stars": {
        "title": "🎮 Brawl Stars",
        "sections": {
            "gems": {
                "title": "💎 Гемы",
                "items": [
                    {"name": "💎 30 гемов", "price": 223},
                    {"name": "💎 80 гемов", "price": 558},
                    {"name": "💎 170 гемов", "price": 1119},
                    {"name": "💎 360 гемов", "price": 2237},
                    {"name": "💎 950 гемов", "price": 5596},
                    {"name": "💎 2000 гемов", "price": 11192},
                ],
            },
            "pass": {
                "title": "🎫 Brawl Pass",
                "items": [
                    {"name": "🎫 Brawl Pass", "price": 1006},
                    {"name": "⭐ Brawl Pass Plus", "price": 1454},
                ],
            },
        },
    },
    "roblox": {
        "title": "🟩 Roblox",
        "sections": {
            "robux": {
                "title": "💸 Robux",
                "items": [
                    {"name": "💸 400 Robux", "price": 559},
                    {"name": "💸 800 Robux", "price": 1118},
                    {"name": "💸 1 700 Robux", "price": 2238},
                    {"name": "💸 4 500 Robux", "price": 5596},
                    {"name": "💸 10 000 Robux", "price": 11192},
                    {"name": "💸 22 500 Robux", "price": 22386},
                ],
            },
        },
    },
}

DB_PATH = "shop.db"
