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
from config import MONGO_URL
from Plugins import LOGGER as log
from Plugins.database.mongo import Mongo

DB = None
if MONGO_URL:
    log.info('[MongoDB] Bağlantı başarılı, oturum başlatıldı')
    DB = Mongo(MONGO_URL)
