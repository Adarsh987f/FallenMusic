from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/indian_best_english_chatting")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Rabgloveu")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7047834233").split()))


FAILED = "https://graph.org/file/7493a3d1bb12165a6f3b3.jpg"
