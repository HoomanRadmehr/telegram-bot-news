import telegram # this is from python-telegram-bot package
import asyncio
from news import gather_translated_news

TELEGRAM = {
    'bot_token' : '5822034614:AAFbZ3bACROgLmZVW_r27_3aLmg3XdfHDzc',
    'channel_name' : 'soulmarines'
}

def create_message_from_news(news):
    titile = news['title']
    discription = news['discription']
    link = news['link']
    image = news['image']
    media = news['media']
    text = f"<strong>{titile}</strong>"+"\n"+"\n"+"\n"+f"{discription}"+"\n"+"\n"+"منبع"+"\n"+f"{media}"+"\n"+f"{link}"+"\n"
    return text

def post_event_on_telegram():
    telegram_settings = TELEGRAM
    bot = telegram.Bot(token=telegram_settings['bot_token'])
    newses = gather_translated_news()
    for news in newses:
        text = create_message_from_news(news)
        bot.send_message(chat_id="@%s" % telegram_settings['channel_name'],text=text,parse_mode=telegram.ParseMode.HTML)

def run():
    post_event_on_telegram()
    
run()
