from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/Disney_storeDan"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=f"https://t.me/musik_supportdan"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/mhmdwldnnnn"),
            InlineKeyboardButton(text=_["S_B_2"], url=f"https://t.me/musik_supportdan"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=f"https://t.me/Disney_storeDan"),
        ],
    ]
    return buttons
