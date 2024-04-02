from ..config import Telegram
from pyrogram import Client

if Telegram.SECONDARY:
    plugins=None
    no_updates=True
else:    
    plugins={"root": "FileStream/bot/plugins"}
    no_updates=None
app =  Client("USERBOT", api_id=29245668,api_hash="53f6d669e7f3e872a00a65dc0686eeac",session_string="BQBPgcAigve1nf9akWoSrGo0SHRxzY46Lbt66ZgtM6VdEi1yrHiVYFn6nFJ10l5p_C-o8StFLqWIxjMxwxyPuM98bLJVp0xnAFB7jqHYTxX2um0af_6_Qpv_HPZqyaszDXwaUCyoynguxYrGd3dwnGv2LQuLCaTraWlAHbC5LoWkK7s_pDuv9vv1ApacSW00bwk7w2GSFcc97IeMKmbC5h-zwrlFnTC2Rt5X5KF_392id52H-Kn1eL18-NemYCYJ0_brtCZVlq4SHT98TarRR25AEjWqEnYS0JImGYHAdGEfJ29HS5qJ_C2nK6yFuqGWjoJCG8Vai3QOdSnATsvCOdmLTywDjQA")
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

