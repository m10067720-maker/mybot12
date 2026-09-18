# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CATALOG, CURRENCY

def categories_kb() -> InlineKeyboardMarkup:
    rows = []
    for cat_key, cat in CATALOG.items():
        rows.append([InlineKeyboardButton(text=cat["title"], callback_data=f"cat:{cat_key}")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def sections_kb(cat_key: str) -> InlineKeyboardMarkup:
    cat = CATALOG[cat_key]
    rows = []
    for sec_key, sec in cat["sections"].items():
        rows.append([InlineKeyboardButton(text=sec["title"], callback_data=f"sec:{cat_key}:{sec_key}")])
    rows.append([InlineKeyboardButton(text="⬅️ Назад", callback_data="back:categories")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

def items_kb(cat_key: str, sec_key: str) -> InlineKeyboardMarkup:
    items = CATALOG[cat_key]["sections"][sec_key]["items"]
    rows = []
    for i, item in enumerate(items):
        rows.append([InlineKeyboardButton(text=f"{item["name"]} — {item["price"]} {CURRENCY}", callback_data=f"item:{cat_key}:{sec_key}:{i}")])
    rows.append([InlineKeyboardButton(text="⬅️ Назад", callback_data=f"back:sections:{cat_key}")])
    return InlineKeyboardMarkup(inline_keyboard=rows)
