# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio

from pyrogram import filters

import config
from strings import get_command
from AlexaMusic import app
from AlexaMusic.misc import SUDOERS
from AlexaMusic.utils.database.memorydatabase import get_video_limit
from AlexaMusic.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")

# إضافة الأمر العربي "المتغيرات"
if isinstance(VARS_COMMAND, str):
    VARS_COMMAND = [VARS_COMMAND, "المتغيرات"]
elif isinstance(VARS_COMMAND, list):
    VARS_COMMAND.append("المتغيرات")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text("يـرجـى الانـتـظـار ... جـاري جـلـب مـتـغـيـرات الـتـكـويـن ...")
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[الـسـورس]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    ass = "نـعـم" if config.AUTO_LEAVING_ASSISTANT == str(True) else "لا"
    pvt = "نـعـم" if config.PRIVATE_BOT_MODE == str(True) else "لا"
    a_sug = "نـعـم" if config.AUTO_SUGGESTION_MODE == str(True) else "لا"
    down = "نـعـم" if config.AUTO_DOWNLOADS_CLEAR == str(True) else "لا"
    git = f"[الـسـورس]({config.GITHUB_REPO})" if config.GITHUB_REPO else "لا"
    if not config.START_IMG_URL:
        start = "لا"
    else:
        start = f"[صـورة]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "لا"
    else:
        s_c = f"[قـنـاة]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "لا"
    else:
        s_g = f"[دَعـم]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "لا"
    else:
        token = "نـعـم"
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        sotify = "لا"
    else:
        sotify = "نـعـم"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**مـتـغـيـرات بـوت الـمـوسـيـقـى :**

**<u>الأسـاسـيـة :</u>**
**MUSIC_BOT_NAME** : `{bot_name}`
**DURATION_LIMIT** : `{play_duration} دقـيـقـة`
**SONG_DOWNLOAD_DURATION_LIMIT** :` {song} دقـيـقـة`
**OWNER_ID** : `{owner_id}`
    
**<u>الـسـورس :</u>**
**UPSTREAM_REPO** : `{up_r}`
**UPSTREAM_BRANCH** : `{up_b}`
**GITHUB_REPO** :` {git}`
**GIT_TOKEN**:` {token}`


**<u>الـبـوت :</u>**
**AUTO_LEAVING_ASSISTANT** : `{ass}`
**ASSISTANT_LEAVE_TIME** : `{auto_leave} ثـانـيـة`
**AUTO_SUGGESTION_MODE** :` {a_sug}`
**AUTO_SUGGESTION_TIME** : `{auto_sug} ثـانـيـة`
**AUTO_DOWNLOADS_CLEAR** : `{down}`
**PRIVATE_BOT_MODE** : `{pvt}`
**YOUTUBE_EDIT_SLEEP** : `{yt_sleep} ثـانـيـة`
**TELEGRAM_EDIT_SLEEP** :` {tg_sleep} ثـانـيـة`
**CLEANMODE_MINS** : `{cm} دقـيـقـة`
**VIDEO_STREAM_LIMIT** : `{v_limit} مـحـادثـة`
**SERVER_PLAYLIST_LIMIT** :` {playlist_limit}`
**PLAYLIST_FETCH_LIMIT** :` {fetch_playlist}`

**<u>سـبـوتـيـفـاي :</u>**
**SPOTIFY_CLIENT_ID** :` {sotify}`
**SPOTIFY_CLIENT_SECRET** : `{sotify}`

**<u>أحـجـام الـمـلـفـات :</u>**
**TG_AUDIO_FILESIZE_LIMIT** :` {tg_aud}`
**TG_VIDEO_FILESIZE_LIMIT** :` {tg_vid}`

**<u>إضـافـيـة :</u>**
**SUPPORT_CHANNEL** : `{s_c}`
**SUPPORT_GROUP** : ` {s_g}`
**START_IMG_URL** : ` {start}`
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
