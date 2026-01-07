# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from os import listdir, mkdir
from os.path import isdir
from shutil import rmtree

from ..logging import LOGGER


def dirr():
    current_items = listdir()

    if "assets" not in current_items:
        LOGGER(__name__).warning(
            "🥀 تحذير: لم يتم العثور على مجلد (Assets) الضروري. يرجى إعادة استنساخ المستودع (Clone) مرة أخرى لضمان عمل البوت بشكل صحيح."
        )
        exit()

    for folder in ("downloads", "cache"):
        if folder in current_items and isdir(folder):
            rmtree(folder)
        mkdir(folder)

    LOGGER(__name__).info("🧚 تم تحديث مجلدات التخزين المؤقت والتنزيلات بنجاح، البوت جاهز للعمل الآن.")
