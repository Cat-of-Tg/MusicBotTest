from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**ʜᴇʏ, ɪ'ᴍ {bn} 
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ  ɢʀᴏᴜᴩ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ[.](https://telegra.ph/file/f9a4e08dc4f58cc86e57e.jpg)
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜsɪᴄ ғʀᴇᴇʟʏ!**""",
        reply_markup=InlineKeyboardMarkup(
          [
              [
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url="https://t.me/team_lad"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url="https://t.me/lezy_music_bot?startgroup=true"
                    )
                ],[
                   
             
                  InlineKeyboardButton(
                     "ᴀssɪsᴛᴀɴᴛ", url="https://t.me/lezy_assistant"
                  ),
              ]
         ]
               
 
            
        ),
     disable_web_page_preview=False
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ᴠᴏᴏᴏ [ɪ ᴍ](t.me/tyra_vcRobot) ᴏɴʟɪɴᴇ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ", url="https://cat_of_tg")
                ]
            ]
        )
   )
