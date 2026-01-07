# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram import filters

import config
from strings import get_command
from AlexaMusic import app
from AlexaMusic.misc import SUDOERS
from AlexaMusic.utils.database import autoend_off, autoend_on
from AlexaMusic.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    # تم تعريب رسالة الاستخدام وإزالة العلامة /
    usage = "**طـريـقـة الاسـتـخـدام :**\n\nانهاء تلقائي [تفعيل|تعطيل]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    
    # تم تعديل الشرط ليقبل كلمة "enable" أو "تفعيل"
    if state in ["enable", "تفعيل"]:
        await autoend_on()
        await message.reply_text(
            "تـم تـفـعـيـل الإغـلاق الـتـلـقـائـي .\n\nسـيـغـادر الـحـسـاب الـمـسـاعـد الـمـحـادثـة الـصـوتـيـة تـلـقـائـيـاً بـعـد بـضـع دقـائـق عـنـد عـدم وجـود أي شـخـص فـي الـمـكـالـمـة ."
        )
    # تم تعديل الشرط ليقبل كلمة "disable" أو "تعطيل"
    elif state in ["disable", "تعطيل"]:
        await autoend_off()
        await message.reply_text("تـم تـعـطـيـل الإغـلاق الـتـلـقـائـي .")
    else:
        await message.reply_text(usage)
