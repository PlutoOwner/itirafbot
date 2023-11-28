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
import logging
import sys
from telethon import TelegramClient
from telethon import TelegramClient, events
from config import APP_ID, API_HASH, BOT_TOKEN




logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)



logging.getLogger("telethon").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)


if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "Python sürümünün en az 3.6 olması GEREKİR! Birçok özellik buna bağlıdır. Bot bırakılıyor."
    )
    quit(1)



bot = TelegramClient('pluto', api_id=APP_ID, api_hash=API_HASH)
pluto = bot.start(bot_token=BOT_TOKEN)



