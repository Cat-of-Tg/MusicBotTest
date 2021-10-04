from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIFN2FaVSk4k7VtwVXO2Tn0fScV26-dAAKrBQACca\_RVoKVRhHdAy67IQQ")
    await message.reply_text(
        f"""*ʜᴇʏ, ɪᴍ'{bn} 
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ  ɢʀᴏᴜᴩ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. 
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜsɪᴄ ғʀᴇᴇʟʏ!**

        """,
        reply_markup=InlineKeyboardMarkup(
            [,[
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url="https://t.me/TeamLadz_bothub"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url="https://t.me/team_lad"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url="https://t.me/lezy_music_bot?startgroup=true"
                    )
                ],[
                   InlineKeyboardButton(
                       "ᴏᴡɴᴇʀ",url="https://t.me/"ok_bie_bot")
                   )
               ],[
                  InlineKeyboardButton(
                     "ᴀssɪsᴛᴀɴᴛ"url="https://t.me/lezy_assistant"
                  ),
                InlineKeyboardButton(
                    "ᴄᴀᴛ ʜᴜʙ"url="https://t.me/cat_of_tg"
                    )
                 ]
        
               
 
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴠᴏᴏᴏ iᴍ ᴏɴʟɪɴᴇ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ", url="https://cat_of_tg")
                ]
            ]
        )
   )
