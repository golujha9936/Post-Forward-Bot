import logging
logger = logging.getLogger(__name__)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from bot import channelforward
from config import Config
from translation import Translation


url_button=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("🥀𝐔ᴘᴅᴀᴛᴇ 𝐂ʜᴀɴɴᴇʟ✨", url='https://t.me/Ace_networkop'), 
                  InlineKeyboardButton("✨𝐒ᴜᴘᴘᴏʀᴛ✨", url='https://t.me/About_Aryan_Owner')
              ]
        ]
) 
################################################################################################################################################################################################################################################
# start command

@channelforward.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message):
    await message.reply(
        text=Translation.START,
        disable_web_page_preview=True,
        reply_markup = url_button,
        quote=True
    )

################################################################################################################################################################################################################################################
# about command

@channelforward.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(client, message):
    await message.reply(
        text=Translation.ABOUT,
        disable_web_page_preview=True,
        reply_markup = url_button,
        quote=True
    )

################################################################################################################################################################################################################################################
