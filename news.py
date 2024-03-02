from GoogleNews import GoogleNews
from googletrans import Translator
from settings import TELEGRAM_BOT_NEWS_TARGET,TELEGRAM_BOT_NEWS_PERIOD


def gather_news():
    google_news = GoogleNews(lang = 'en', period=TELEGRAM_BOT_NEWS_PERIOD)
    google_news.search(TELEGRAM_BOT_NEWS_TARGET)
    results = google_news.result()
    return results
    
def gather_translated_news():
    translator = Translator()
    translated_titles = []
    newses = gather_news()
    for i in range(len(newses)):
        translated_title_news = translator.translate(newses[i]["title"], src='en', dest='fa').text
        translated_discription_news = translator.translate(newses[i]["desc"], src='en', dest='fa').text
        link = newses[i]['link']
        image = newses[i]['img']
        media = newses[i]['media']
        obj = {'title':translated_title_news,'discription':translated_discription_news,'link':link,"image":image,'media':media}
        translated_titles.append(obj)
    return translated_titles
