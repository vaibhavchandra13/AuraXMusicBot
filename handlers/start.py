from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
I am Grijze a Music Player Bot, an open-source bot that lets you play music in your Telegram groups.
Created By @GrijzeWolfXD
For Support Join Our Channel @GrijzeBots.
Use the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="https://telegra.ph/Commands-06-03",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/GrijzeWolfXD"
                    ),
                    InlineKeyboardButton(
                        "Instagram", url="http://instagram.com/alone.wolf.ig"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Join Channel", url="https://t.me/GrijzeBots"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Hey, I am Grijze a Music Bot. Note : Please make me admin",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Instagram", url="http://instagram.com/alone.wolf.ig"
                    )
                ]
            ]
        )
    )
