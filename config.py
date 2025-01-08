from os import getenv


API_ID = int(getenv("API_ID", "27439638"))
API_HASH = getenv("API_HASH", "ce0b3293fb021531e92fe6341f2f1a15")
BOT_TOKEN = getenv("BOT_TOKEN", "7433470507:AAExGKou43O1IQq0Qdk7oR3mMwL6SeCV6gE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7899717596").split()))
MONGO_DB = getenv("MONGO_DB", "")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002287517477"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", ""))


