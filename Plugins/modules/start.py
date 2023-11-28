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
import io
import re

 
from Plugins import pluto
from telethon import events, Button
from telethon.tl.functions.messages import SendMessageRequest

from config import kanal, log_qrup, owner, support 

from Plugins.database import DB
from Plugins.modules.mesaj.message import startmesaj, qrupstart 


@pluto.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in pluto.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     id = event.sender_id
     await DB.add_user(id)
     await pluto.send_message(log_qrup, f"ℹ️ **Yeni Kullanıcı -** {ad}")
     return await event.reply(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("💌 İtiraf Yaz", data="itiraf")
                      ],
                      [Button.url('📜 İtiraf Kanalı', f'https://t.me/{kanal}')],
                      [Button.url('💬 Destek', f'https://t.me/{support}'),
                       Button.url('👤 Owner', f'https://t.me/{owner}')]
                    ),
                    link_preview=False)
     
   

    



