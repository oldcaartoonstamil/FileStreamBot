from ..config import Telegram
from pyrogram import Client

if Telegram.SECONDARY:
    plugins=None
    no_updates=True
else:    
    plugins={"root": "FileStream/bot/plugins"}
    no_updates=None
app =  Client("USERBOT", api_id=29245668,api_hash="53f6d669e7f3e872a00a65dc0686eeac",session_string="Telegram.SESSION")
FileStream=Client(
    name="FileStream",
    api_id=Telegram.API_ID,
    api_hash=Telegram.API_HASH,
    workdir="FileStream",
    plugins=plugins,
    bot_token=Telegram.BOT_TOKEN,
    sleep_threshold=Telegram.SLEEP_THRESHOLD,
    workers=Telegram.WORKERS,
    no_updates=no_updates
    )

multi_clients = {}
work_loads = {}

