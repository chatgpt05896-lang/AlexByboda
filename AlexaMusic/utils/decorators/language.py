# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from strings import get_string
from AlexaMusic.misc import SUDOERS
from AlexaMusic.utils.database import get_lang, is_commanddelete_on, is_maintenance


def language(mystic):
    async def wrapper(_, message, **kwargs):
        if await is_maintenance() is False and message.from_user.id not in SUDOERS:
            return await message.reply_text(
                "🧚 عذراً، البوت في وضع الصيانة حالياً لإجراء التحديثات اللازمة. يرجى المحاولة في وقت لاحق."
            )
        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except Exception:
                pass
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except Exception:
            # تم التغيير لـ ar
            language = get_string("ar")
        return await mystic(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if (
            await is_maintenance() is False
            and CallbackQuery.from_user.id not in SUDOERS
        ):
            return await CallbackQuery.answer(
                "🧚 عذراً، البوت في وضع الصيانة حالياً لإجراء التحديثات اللازمة. يرجى المحاولة في وقت لاحق.",
                show_alert=True,
            )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except Exception:
            # تم التغيير لـ ar
            language = get_string("ar")
        return await mystic(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except Exception:
            # تم التغيير لـ ar
            language = get_string("ar")
        return await mystic(_, message, language)

    return wrapper
