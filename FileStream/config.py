from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = 29245668
    API_HASH = "53f6d669e7f3e872a00a65dc0686eeac"
    BOT_TOKEN = "6455795402:AAECZkl17Y8TK_H8SPt947tjame4ZaQ8-lM"
    OWNER_ID = 1328284557
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = "mongodb+srv://oldfilestorebot:ofsb@cluster0.myqdttg.mongodb.net/?retryWrites=true&w=majority"
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "media_links"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream112'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    START_PIC = env.get('START_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", -1001806967645))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", -1001806967645))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", 'filestreambott-37990de3fe0d.herokuapp.com'))
    URL = "https://{}/".format(FQDN)
