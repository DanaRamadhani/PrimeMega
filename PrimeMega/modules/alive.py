import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from PrimeMega.events import register
from PrimeMega import telethn as tbot


PHOTO = "https://telegra.ph/file/e07911f2bde1fb0cf562c.jpg"

@register(pattern=("/alive"))
async def awake(event):
  PRIME = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm PINKYMEKS ID.** \n\n"
  PRIME += "⚪ **I'm Working Properly** \n\n"
  PRIME += f"⚪ **My Beby : [Beby](https://t.me/Bbymaura)** \n\n"
  PRIME += f"⚪ **Library Version :** `{telever}` \n\n"
  PRIME += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  PRIME += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  PRIME += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/PinkyMeksRobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/pinkymeksch")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PRIME,  buttons=BUTTON)
