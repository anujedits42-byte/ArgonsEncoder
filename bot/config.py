# Developed by ARGON telegram: @REACTIVEARGON
import os

from dotenv import load_dotenv

load_dotenv()


# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8564884831:AAF0ksogvIew4CDv5N8HcSJOq-vkCrrAOHk")
# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "34446649"))  # Placeholder ID
# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
# Your db channel Id
LOG_CHANNEL = int(os.environ.get("CHANNEL_ID", "-1003515041061"))  # Placeholder channel ID
# NAMA OWNER
OWNER = os.environ.get("OWNER", "@anujedits76")
# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7892805795"))  # Placeholder owner ID
# Port
PORT = os.environ.get("PORT", "8030")
# Database
DB_URI = os.environ.get(
    "DATABASE_URL",
    "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0",  # Placeholder DB URI
)
DB_NAME = os.environ.get("DATABASE_NAME", "Anujedit")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))
