from dotenv import load_dotenv
import os


load_dotenv()

TELEGRAM_BOT_CHANNEL_NAME=os.getenv("TELEGRAM_BOT_CHANNEL_NAME")
TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_BOT_NEWS_TARGET=os.getenv("TELEGRAM_BOT_NEWS_TARGET")
TELEGRAM_BOT_NEWS_PERIOD=os.getenv("TELEGRAM_BOT_NEWS_PERIOD")
