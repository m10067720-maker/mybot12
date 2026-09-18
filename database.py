# -*- coding: utf-8 -*-

import aiosqlite
from datetime import datetime
from config import DB_PATH

CREATE_USERS = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    full_name TEXT,
    created_at TEXT
);
"""

CREATE_ORDERS = """
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    username TEXT,
    category TEXT,
    item_name TEXT,
    price INTEGER,
    game_login TEXT,
    status TEXT DEFAULT "awaiting_payment",
    admin_chat_msg_id INTEGER,
    created_at TEXT
);
"""

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(CREATE_USERS)
        await db.execute(CREATE_ORDERS)
        await db.commit()

async def upsert_user(user_id: int, username: str, full_name: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO users (user_id, username, full_name, created_at) VALUES (?, ?, ?, ?) "
            "ON CONFLICT(user_id) DO UPDATE SET username=excluded.username, full_name=excluded.full_name",
            (user_id, username, full_name, datetime.utcnow().isoformat())
        )
        await db.commit()

async def create_order(user_id: int, username: str, category: str, item_name: str, price: int, game_login: str) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "INSERT INTO orders (user_id, username, category, item_name, price, game_login, status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (user_id, username, category, item_name, price, game_login, "awaiting_payment", datetime.utcnow().isoformat())
        )
        await db.commit()
        return cursor.lastrowid

async def set_order_admin_msg(order_id: int, msg_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE orders SET admin_chat_msg_id=? WHERE order_id=?", (msg_id, order_id))
        await db.commit()

async def set_order_status(order_id: int, status: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE orders SET status=? WHERE order_id=?", (status, order_id))
        await db.commit()

async def get_order(order_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute("SELECT * FROM orders WHERE order_id=?", (order_id,))
        return await cursor.fetchone()

async def get_user_orders(user_id: int, limit: int = 10):
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute("SELECT * FROM orders WHERE user_id=? ORDER BY order_id DESC LIMIT ?", (user_id, limit))
        return await cursor.fetchall()
