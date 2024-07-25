import os

# Pyrogram API credentials
API_ID = int(os.environ.get("API_ID", 29426486))
API_HASH = os.environ.get("API_HASH", "d71ad4ec048ab41677a1a439b21ff0c9")

# Bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7355006985:AAEY8ijg4CP-8GgcliRGJja87Tby78QT7To")

# Pyrogram session name
SESSION_NAME = os.environ.get("bot")

# MongoDB URI (if you're using MongoDB)
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")
 