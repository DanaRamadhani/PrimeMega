from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from PrimeMega import pbot
from PrimeMega.utils.errors import capture_err
from PrimeMega.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_text(
        f"""✨ **Hey I'm PINKYMEKS ID** 
**Owner repo : [ BEBY ](https://t.me/Bbymaura)**
**Python Version :** `{y()}`
**Library Version :** `{o}`
**Telethon Version :** `{s}`
**Pyrogram Version :** `{z}`
**Create your own with click button bellow.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ʀᴇᴘᴏ", url="www.xnxx.com"), 
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/pinkymeksch")
                ]
            ]
        ),
        disable_web_page_preview=True
    )
