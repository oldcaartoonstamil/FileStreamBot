from ..config import Telegram
from pyrogram import Client

if Telegram.SECONDARY:
    plugins=None
    no_updates=True
else:    
    plugins={"root": "FileStream/bot/plugins"}
    no_updates=None
app =  Client("USERBOT", api_id=9871107,api_hash="6277e562fe3ca0533e152e9f45f70906",session_string=Telegram.SESSION)
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

