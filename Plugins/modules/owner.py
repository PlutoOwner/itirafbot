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
import asyncio
from telethon import events, errors
from Plugins import pluto as bot
from Plugins.database import DB

from config import SUDOERS




@bot.on(events.NewMessage(pattern=r"/broadcast\s*([\s\S]*)?"))
async def broadcast(event):
    if not DB:
        await event.reply('Önce Mongo URL -sini Ekleyin')
        return
    if not (event.sender_id in SUDOERS):
        return
    text = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not (text or reply):
        return await event.reply('Lütfen Bir Mesaj Gönderin veya Mesaja Cevap Verin')
    sent = 0
    ids = await DB.get_users()

    msg = await event.reply(
        "**İşleniyor....\nLütfen Yanıtlanan Mesajı Silmeyin**"
    ) if reply else await event.reply('**İşleniyor....**')
    for user in ids:
        try:
            await reply.forward_to(user) if reply else await bot.send_message(
                user, text)
            sent += 1
            await asyncio.sleep(0.8)
        except errors.rpcerrorlist.FloodWaitError as fwerr:
            await asyncio.sleep(fwerr.seconds + 5)
        except Exception:
            continue

    result = f"**Toplam {len(ids)} Kişiye Gönderildi**"
    try:
        await msg.edit(result)
    except:
        await event.reply(result)
