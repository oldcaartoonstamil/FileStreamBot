from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = 1
    API_HASH = "2"
    BOT_TOKEN = "fuck you 🖕"
    OWNER_ID = 1328284557
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL="🖕"
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "media_links"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'filestream'))
    FORCE_SUB_ID = -1001304669315
    FORCE_SUB = True
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
    FILE_PIC = env.get('FILE_PIC', "https://telegra.ph/file/7de19fc3f09d19ddbf823.jpg")
    START_PIC = env.get('START_PIC', "https://telegra.ph/file/7de19fc3f09d19ddbf823.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://telegra.ph/file/7de19fc3f09d19ddbf823.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", -1002027926399))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", -1002027926399))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))
class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", 'medialinksstreaming-7114655cf755.herokuapp.com'))
    URL = "https://{}/".format(FQDN)
