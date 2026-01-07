# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = [
    InlineQueryResultArticle(
        title="إيـقـاف مـؤقـت",
        description="لإيـقـاف الـتـشـغـيـل الـحـالـي مـؤقـتـاً فـي الـمـكـالـمـة.",
        thumb_url="https://files.catbox.moe/exvq3d.jpg",
        input_message_content=InputTextMessageContent("/pause"),
    ),
    InlineQueryResultArticle(
        title="اسـتـئـنـاف",
        description="لاسـتـئـنـاف الـتـشـغـيـل الـمـتـوقـف فـي الـمـكـالـمـة.",
        thumb_url="https://files.catbox.moe/kmn0a6.jpg",
        input_message_content=InputTextMessageContent("/resume"),
    ),
    InlineQueryResultArticle(
        title="تـخـطـي",
        description="لـتـخـطـي الـتـشـغـيـل الـحـالـي والـانـتـقـال لـلـتـالـي.",
        thumb_url="https://files.catbox.moe/zs9g3f.jpg",
        input_message_content=InputTextMessageContent("/skip"),
    ),
    InlineQueryResultArticle(
        title="إنـهـاء",
        description="لإنـهـاء الـتـشـغـيـل الـحـالـي ومـغـادرة الـمـسـاعـد.",
        thumb_url="https://files.catbox.moe/b91yyd.jpg",
        input_message_content=InputTextMessageContent("/end"),
    ),
    InlineQueryResultArticle(
        title="خـلـط",
        description="لـخـلـط تـرتـيـب الـأغـانـي فـي قـائـمـة الـانـتـظـار.",
        thumb_url="https://files.catbox.moe/wqipfn.jpg",
        input_message_content=InputTextMessageContent("/shuffle"),
    ),
    InlineQueryResultArticle(
        title="تـكـرار",
        description="لـتـكـرار الـتـشـغـيـل الـحـالـي فـي الـمـكـالـمـة.",
        thumb_url="https://files.catbox.moe/4qhfqw.jpg",
        input_message_content=InputTextMessageContent("/loop 3"),
    ),
]
