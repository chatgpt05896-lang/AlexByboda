# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.
#
# تم تعريب الملف وتطويره بواسطة مطور البوت الخاص بك.
# ☔ ☔ ☔ ☔ ☔ ☔ ☔ ☔ ☔ ☔

import sys
from pyrogram import Client
import config
from ..logging import LOGGER

# ☔ قوائم لتخزين بيانات المساعدين
assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        """
        ☔ تهيئة كلاس البوت المساعد (Userbot).
        يتم هنا تعريف 5 عملاء (Clients) كحد أقصى للعمل كمساعدين في المكالمات.
        """
        self.one = Client(
            name="AlexaOne",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="AlexaTwo",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="AlexaThree",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="AlexaFour",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="AlexaFive",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        """
        ☔ دالة بدء التشغيل الموحدة.
        تقوم بتشغيل الجلسات المتوفرة، وإرسال إشعارات لجروب السجل.
        """
        LOGGER(__name__).info(f"☔ جاري تشغيل حسابات المساعد (Assistants)...")

        # =================================================================
        # ☔ 1. تشغيل الحساب المساعد الأول
        # =================================================================
        if config.STRING1:
            await self.one.start()
            
            # ⛔ تم تعطيل الانضمام لقنوات السورس الأصلي لمنع الإزعاج
            try:
                # await self.one.join_chat("Alexa_Help")
                # await self.one.join_chat("TheTeamAlexa")
                pass 
            except Exception:
                pass
            
            assistants.append(1)
            
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID,
                    "☔ **تم تشغيل الحساب المساعد الأول بنجاح!**\n\n✅ جاهز الآن لتشغيل الموسيقى في المحادثات الصوتية بطلاقة.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"❌ فشل الحساب المساعد [1] في الوصول إلى مجموعة السجل (Logger Group).\n"
                    f"☔ تأكد من إضافة الحساب للمجموعة ورفعه مشرف!"
                )
                sys.exit()
            
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            
            if get_me.last_name:
                self.one.name = get_me.first_name + " " + get_me.last_name
            else:
                self.one.name = get_me.first_name
            
            LOGGER(__name__).info(f"☔ تم بدء المساعد الأول باسم: {self.one.name}")

        # =================================================================
        # ☔ 2. تشغيل الحساب المساعد الثاني
        # =================================================================
        if config.STRING2:
            await self.two.start()
            
            try:
                # await self.two.join_chat("Alexa_Help")
                pass
            except Exception:
                pass
            
            assistants.append(2)
            
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID,
                    "☔ **تم تشغيل الحساب المساعد الثاني بنجاح!**\n\n✅ جاهز الآن لتشغيل الموسيقى في المحادثات الصوتية بطلاقة.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"❌ فشل الحساب المساعد [2] في الوصول إلى مجموعة السجل.\n"
                    f"☔ تأكد من إضافة الحساب للمجموعة ورفعه مشرف!"
                )
                sys.exit()
            
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            
            if get_me.last_name:
                self.two.name = get_me.first_name + " " + get_me.last_name
            else:
                self.two.name = get_me.first_name
            
            LOGGER(__name__).info(f"☔ تم بدء المساعد الثاني باسم: {self.two.name}")

        # =================================================================
        # ☔ 3. تشغيل الحساب المساعد الثالث
        # =================================================================
        if config.STRING3:
            await self.three.start()
            
            try:
                # await self.three.join_chat("Alexa_Help")
                pass
            except Exception:
                pass
            
            assistants.append(3)
            
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID,
                    "☔ **تم تشغيل الحساب المساعد الثالث بنجاح!**\n\n✅ جاهز الآن لتشغيل الموسيقى في المحادثات الصوتية بطلاقة.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"❌ فشل الحساب المساعد [3] في الوصول إلى مجموعة السجل.\n"
                    f"☔ تأكد من إضافة الحساب للمجموعة ورفعه مشرف!"
                )
                sys.exit()
            
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            
            if get_me.last_name:
                self.three.name = get_me.first_name + " " + get_me.last_name
            else:
                self.three.name = get_me.first_name
            
            LOGGER(__name__).info(f"☔ تم بدء المساعد الثالث باسم: {self.three.name}")

        # =================================================================
        # ☔ 4. تشغيل الحساب المساعد الرابع
        # =================================================================
        if config.STRING4:
            await self.four.start()
            
            try:
                # await self.four.join_chat("Alexa_Help")
                pass
            except Exception:
                pass
            
            assistants.append(4)
            
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID,
                    "☔ **تم تشغيل الحساب المساعد الرابع بنجاح!**\n\n✅ جاهز الآن لتشغيل الموسيقى في المحادثات الصوتية بطلاقة.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"❌ فشل الحساب المساعد [4] في الوصول إلى مجموعة السجل.\n"
                    f"☔ تأكد من إضافة الحساب للمجموعة ورفعه مشرف!"
                )
                sys.exit()
            
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            
            if get_me.last_name:
                self.four.name = get_me.first_name + " " + get_me.last_name
            else:
                self.four.name = get_me.first_name
            
            LOGGER(__name__).info(f"☔ تم بدء المساعد الرابع باسم: {self.four.name}")

        # =================================================================
        # ☔ 5. تشغيل الحساب المساعد الخامس
        # =================================================================
        if config.STRING5:
            await self.five.start()
            
            try:
                # await self.five.join_chat("Alexa_Help")
                pass
            except Exception:
                pass
            
            assistants.append(5)
            
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID,
                    "☔ **تم تشغيل الحساب المساعد الخامس بنجاح!**\n\n✅ جاهز الآن لتشغيل الموسيقى في المحادثات الصوتية بطلاقة.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"❌ فشل الحساب المساعد [5] في الوصول إلى مجموعة السجل.\n"
                    f"☔ تأكد من إضافة الحساب للمجموعة ورفعه مشرف!"
                )
                sys.exit()
            
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            
            if get_me.last_name:
                self.five.name = get_me.first_name + " " + get_me.last_name
            else:
                self.five.name = get_me.first_name
            
            LOGGER(__name__).info(f"☔ تم بدء المساعد الخامس باسم: {self.five.name}")
