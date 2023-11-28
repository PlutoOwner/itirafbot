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
from config import kanal 




startmesaj = "\n**Hoş geldin**\n__Kimseye söylemediğiniz itirafları bana anlatabilirsiniz__" 
qrupstart = "✅ **Aktifim!** 💌 **İtiraf yazmak için özelden yazın"
itirafmsg = "**İtirafınızı nasıl paylaşırsınız?** 🤔"
itirafyaz = "**İşte bir itiraf yaz daha sonra herkese açık mı yoksa anonim mi olacağını soracağım** 😍"
start = f"✅ **İtirafınız gönderildi ve yöneticiler tarafından onaylandıktan sonra @{kanal} kanalında paylaşılacaktır**"
gonderildi = f"✅ **İtirafınız gönderildi ve yöneticiler tarafından onaylandıktan sonra @{kanal} kanalında paylaşılacaktır**"
