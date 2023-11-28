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
import codecs
import heroku3
import asyncio
import aiohttp
import math
import os
import ssl
import requests
import random
import base64

import os, logging, asyncio

from Plugins import pluto
from Plugins.modules.mesaj.message import startmesaj, itirafmsg, itirafyaz, start, gonderildi

from telethon.tl.functions import *
from telethon.tl import functions
from asyncio import sleep

from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation

from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.types import InputPeerChat

from config import admin_qrup, itiraf_qrup, kanal, log_qrup, owner, support, botad


itiraf_eden = ["Kullanıcı Seçilmedi"]
mesaj = ["Mesaj Görünmedi"]


@pluto.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in pluto.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("💌 İtiraf Yaz", data="itiraf")
                      ],
                      [Button.url('📜 İtiraf Kanalı', f'https://t.me/{kanal}')],
                      [Button.url('💬 Destek', f'https://t.me/{support}'),
                       Button.url('👤 Owner', f'https://t.me/{owner}')]
                    ),
                    link_preview=False)


@pluto.on(events.callbackquery.CallbackQuery(data="itiraf"))
async def handler(event):
    await event.edit(f"{itirafyaz}", buttons=(
                      [
                      Button.inline("🏠 Ana Sayfa", data="start")
                      ]
                    ),
                    link_preview=False)


@pluto.on(events.NewMessage)
async def yeni_mesaj(event: events.NewMessage.Event):
  global mesaj
  if event.is_private:
    mesaj = str(event.raw_text)
    if not mesaj == "/start":
      await pluto.send_message(event.chat_id, f"{itirafmsg}", buttons=(
                      [
                      Button.inline("🔒 Anonim", data="anonim"),
                      Button.inline("🌟 Açık", data="acik")
                      ],
                      [
                      Button.inline("🏠 Ana Sayfa", data="start")
                      ]
                    ),
                    link_preview=False)
                    
itiraf_anonim = b"\xF0\x9F\x92\x8C\x20\x45\x74\x69\x72\x61\x66\x20\x42\x6F\x74\x0A\xF0\x9F\x93\xB2\x20\x54\x65\x6C\x65\x74\x68\x6F\x6E\x20\x2D\x20\x31\x2E\x32\x34\x2E\x30\x0A\xF0\x9F\x93\xA3\x20\x53\x75\x70\x70\x6F\x72\x74\x20\x2D\x20\x40\x52\x6F\x42\x6F\x74\x6C\x61\x72\x69\x6D\x54\x67\x0A\xF0\x9F\x91\xA8\xF0\x9F\x8F\xBB\xE2\x80\x8D\xF0\x9F\x92\xBB\x20\x4F\x77\x6E\x65\x72\x20\x2D\x20\x40\x61\x79\x6B\x68\x61\x6E\x5F\x73"
@pluto.on(events.callbackquery.CallbackQuery(data="anonim"))
async def anonim(event):
    global mesaj
    global onay
    async for usr in pluto.iter_participants(event.chat_id):
     gonderen = f"[{usr.first_name}](tg://user?id={usr.id})"
     itiraf_eden = "Anonim"
     yeni_itiraf = await pluto.send_message(admin_qrup, f"📣 **Yeni itiraf**\n\n🗣️ **İtiraf Eden -** {itiraf_eden} \n📜 **İtirafı -** {mesaj} \n\n📣 İtirafınızı {botad} -a edin")
     onay = await yeni_itiraf.reply("Yeni İtiraf !!!", buttons=(
                      [
                       Button.inline("✅ Onayla", data="onay"
                       ),
                       Button.inline("🗑️ Sil", data="sil")
                      ]
                    ),
                    link_preview=False)
    await pluto.send_message(log_qrup, f"ℹ️ {gonderen} __Anonim İtiraf Yazdı__")
    await event.edit(f"{gonderildi}", buttons=(
                      [
                       Button.inline("💌 Yeni İtiraf", data="itiraf"),
                       Button.inline("🏠 Ana Sayfa", data="start")
                      ]
                    ),
                    link_preview=False)
anonim = itiraf_anonim.decode("utf8")
 
itiraf_acik = b"\xE2\x84\xB9\xEF\xB8\x8F\x20\x42\x6F\x74\x20\x62\x61\xC5\x9F\x6C\x61\x64\xC4\xB1\x6C\x64\xC4\xB1\x20\x70\x72\x6F\x62\x6C\x65\x6D\x20\x79\x61\x72\x61\x6E\x64\xC4\xB1\x71\x64\x61\x20\x73\x75\x70\x70\x6F\x72\x74\x20\x71\x72\x75\x70\x75\x6E\x61\x20\x79\x61\x7A\xC4\xB1\x6E\x0A\xE2\x9A\xA1\x20\x42\x6F\x74\x75\x6E\x75\x7A\x20\x53\x75\x70\x65\x72\x20\xC4\xB0\xC5\x9F\x6C\x65\x79\x69\x72\x2E\x2E\x2E"
@pluto.on(events.callbackquery.CallbackQuery(data="acik"))
async def aciq(event):
    global mesaj
    global onay
    async for usr in pluto.iter_participants(event.chat_id):
     itiraf_eden = f"[{usr.first_name}](tg://user?id={usr.id})"
     sonluq = f"\n💌 İtirafınızı {botad} -a edin"
     yeni_itiraf = await pluto.send_message(admin_qrup, f"📣 **Yeni itiraf**\n\n🗣️ **İtiraf Eden -** {itiraf_eden} \n📜 **İtirafı -** {mesaj} \n{sonluq}")
     onay = await yeni_itiraf.reply("Yeni İtiraf !!!", buttons=(
                      [
                       Button.inline("✅ Onayla", data="onay"
                       ),
                       Button.inline("🗑️ Sil", data="sil")
                      ]
                    ),
                    link_preview=False)
    await pluto.send_message(log_qrup, f"ℹ️ {itiraf_eden} __Açık İtiraf Yazdı__")
    await event.edit(f"{gonderildi}", buttons=(
                      [
                       Button.inline("💌 Yeni İtiraf", data="itiraf"),
                       Button.inline("🏠 Ana Sayfa", data="start")
                      ]
                    ),
                    link_preview=False)
acik = itiraf_acik.decode("utf8")
  
@pluto.on(events.callbackquery.CallbackQuery(data="onay"))
async def onay(event):
    global onay
    async for usr in pluto.iter_participants(event.chat_id):
      tesdiqliyen = f"[{usr.first_name}](tg://user?id={usr.id})"
    if onay.reply_to_msg_id:
      itiraff = await onay.get_reply_message()
      itiraf = itiraff.text
      await pluto.send_message(itiraf_qrup, itiraf)
      await event.edit(f"✅ **İtiraf Onaylandı**")
      
@pluto.on(events.callbackquery.CallbackQuery(data="sil"))
async def sil(event):
    global onay
    if not onay.is_reply:
      return await onay.edit("HATA!!!")
    if onay.is_reply:
      itiraf = await onay.get_reply_message()
      await itiraf.delete()
      await event.edit("🗑️ İtiraf Silindi")
