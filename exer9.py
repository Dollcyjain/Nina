import json

import requests


def speak(str1):
    from win32com.client import Dispatch
    speak1 = Dispatch("SAPI.SpVoice")
    speak1.Speak(str1)


if __name__ == "__main__":
    headline = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=d5e09fa0cfac46fc92c159a89960596e")
    data = headline.text
    parsed = json.loads(data)
    # speak(parsed)
    i = 0
    while i < 10:
        news = parsed['articles'][i]['title']
        newslist = parsed['articles'][i]['title'].split(" - ")
        print(f"{i+1}. {newslist[0]}")
        speak(f"{i+1}")
        speak(f"{newslist[0]}")
        i += 1
