# -*- coding: utf-8 -*-

# (c) @PlutoOwner-github (Github) | https://t.me/PlutoOwner | @PlutoKanal (Telegram)

# ==============================================================================
#
# Proje: @itirafimbot
# Telif Hakkı (C) 2023 PlutoOwner-Github@Github, <https://github.com/PlutoOwner-github>.
#
# Bu dosya <https://github.com/PlutoOwner/itirafbot> projesinin bir parçası,
# ve "GNU V3.0 Lisans Sözleşmesi" kapsamında yayınlanır.
# Lütfen bkz. < https://github.com/PlutoOwner/itirafbot/blob/master/LICENSE >
#
#
# ========================================================================
import os
import heroku3
from telethon import TelegramClient, events


APP_ID = int(os.environ.get("APP_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("TOKEN")

admin_qrup = int(os.environ.get("admin_qrup"))
itiraf_qrup = int(os.environ.get("itiraf_qrup"))
kanal = os.environ.get("kanal")
log_qrup = int(os.environ.get("log_qrup"))
botad = os.environ.get("botad")
support = os.environ.get("support")
owner = os.environ.get("owner")

SUDOERS = list(map(int, os.environ.get("SUDOERS", 0).split()))
MONGO_URL = os.environ.get("MONGO_URL", None)
