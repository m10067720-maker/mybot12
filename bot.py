print("DEBUG BOT_TOKEN len:", len(__import__("os").getenv("BOT_TOKEN") or ""))
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

import config
import database as db
import keyboards as kb

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await db.upsert_user(message.from_user.id, message.from_user.username or "", message.from_user.full_name)
    await message.answer("👋 Привет! Добро пожаловать в магазин!", reply_markup=kb.categories_kb())

async def main():
    await db.init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
