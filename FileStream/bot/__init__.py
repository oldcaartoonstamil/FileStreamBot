from ..config import Telegram
from pyrogram import Client

if Telegram.SECONDARY:
    plugins=None
    no_updates=True
else:    
    plugins={"root": "FileStream/bot/plugins"}
    no_updates=None
    
class User(Client):
    def __init__(self):
        super().__init__(
            name="user",
            api_hash=Telegram.API_HASH,
            api_id=Telegram.APP_ID,
            workers=Telegram.WORKERS
        )
        self.LOGGER = LOGGER
        
    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started! \n\nSend a message in your channel now!!"
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")

class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            name="FileStream1",
            api_id=Telegram.API_ID,
            api_hash=Telegram.API_HASH,
            workdir="FileStream",
            plugins=plugins,
            bot_token=Telegram.BOT_TOKEN,
            sleep_threshold=Telegram.SLEEP_THRESHOLD,
            workers=Telegram.WORKERS,
            no_updates=no_updates
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()
        await self.USER.send_message(
            chat_id=usr_bot_me.username,
            text="😬🤒🤒"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
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

