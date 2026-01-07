# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import BANNED_USERS
from strings import get_command, get_string, languages_present
from AlexaMusic import app
from AlexaMusic.utils.database import get_lang, set_lang
from AlexaMusic.utils.decorators import ActualAdminCB, language, languageCB

# Languages Available


def lanuages_keyboard(_):
    buttons = [
        InlineKeyboardButton(text=languages_present[i], callback_data=f"languages:{i}")
        for i in languages_present
    ]
    keyboardx = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]

    keyboardx.append(
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"], callback_data="settingsback_helper"
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ]
    )
    return InlineKeyboardMarkup(keyboardx)


LANGUAGE_COMMAND = get_command("LANGUAGE_COMMAND")


@app.on_message(filters.command(LANGUAGE_COMMAND) & filters.group & ~BANNED_USERS)
@language
async def langs_command(client, message: Message, _):
    keyboard = lanuages_keyboard(_)
    await message.reply_text(
        _["setting_1"].format(message.chat.title, message.chat.id),
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex("LG") & ~BANNED_USERS)
@languageCB
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except Exception:
        pass
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"languages:(.*?)") & ~BANNED_USERS)
@ActualAdminCB
async def language_markup(client, CallbackQuery, _):
    langauge = CallbackQuery.data.split(":")[1]
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer(
            f"🧚 يا {CallbackQuery.from_user.first_name}، أنت بالفعل تستخدم هذه اللغة في المجموعة، لا داعي لتغييرها مرة أخرى.", show_alert=True
        )
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer(
            f"🤍 تم تغيير لغة البوت بنجاح إلى اللغة المختارة يا {CallbackQuery.from_user.first_name}، استمتع بالتجربة.", show_alert=True
        )
    except Exception:
        return await CallbackQuery.answer(
            "🥀 عذراً، فشل البوت في تغيير اللغة حالياً أو أنها قيد الصيانة، يرجى المحاولة في وقت لاحق.",
            show_alert=True,
        )
    await set_lang(CallbackQuery.message.chat.id, langauge)
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)
