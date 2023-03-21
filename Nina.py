import datetime
import speech_recognition as sr
import wikipedia
import pyttsx3
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    """Its gives a speech output of the audio given as an argument"""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """It greets the user according to time as speech output."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Good Morning!!")
        speak("Good Morning!!")
    elif 12 <= hour < 18:
        print("Good Afternoon!!")
        speak("Good Afternoon!!")
    else:
        print("Good Evening!!")
        speak("Good Evening!!")
    print("I am Nina. Please tell me how may I help you?")
    speak("I am Nina. Please tell me how may I help you?")


def takeCommand():
    """It takes speech input from the user and return string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in', show_all=True)['alternative'][0]['transcript']
        print(f"User: {query}")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    # speak('open pycharm')
    # speak('Taj Mahal wikipedia')
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching in wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            print("Nina: According to Wikipedia...")
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            print("Nina: Opening Youtube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("Nina: Opening Google...")
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            print("Nina: Opening Stackoverflow...")
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Nina: The time is {strTime}")
            speak(f"The time is {strTime}")
        elif 'google' in query:
            query = query.replace("google", '')
            query = query.replace("nina", '')
            webbrowser.open(f"www.google.com/search?client=firefox-b-d&q={query.replace(' ', '+')}")
        elif 'open code' in query:
            print("Nina: Opening VS Code")
            codePath = r"C:\Users\dola\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'open pie charm' in query:
            print("Nina: Opening Pycharm")
            charmPath = r"C:\Program Files\JetBrains\PyCharm Community Edition 2022.1.1\bin\pycharm64.exe"
            os.startfile(charmPath)
        elif 'open firefox' in query:
            print("Nina: Opening Firefox")
            firePath = r"C:\Program Files\Mozilla Firefox\firefox.exe"
            os.startfile(firePath)
        elif 'open python playlist' in query:
            print("Nina: Opening python playlist")
            webbrowser.open("www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")
        elif 'open data structure playlist' in query:
            print("Nina: Opening Data Structure and Algorithm playlist")
            webbrowser.open("www.youtube.com/playlist?list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi")
        elif 'open my batches' in query:
            print("Nina: Opening Physics Wallah: Your Batches")
            webbrowser.open("https://www.pw.live/study/batches/study/my-batches")
        elif 'news' in query:
            try:
                print("Nina: Opening News..")
                os.startfile(r"c:\Users\dola\PycharmProjects\pythonLang\exer9.py")
            except Exception as e:
                print("Nina: Sorry, I am not able to open news.")
                speak("Sorry, I am not able to open news.")
        elif 'open hackerrank' in query:
            print("Nina: Opening Hakerrank")
            webbrowser.open("www.hackerrank.com/dashboard")
        elif 'new folder' in query:
            print("Nina: What will be the name of new folder?")
            speak("What will be the name of new folder?")
            name = takeCommand().lower()
            try:
                if name != "none":
                    os.mkdir(f'C:\\Users\\dola\\Desktop\\{name}')
                    print(f"Nina: I successfully made {name} folder.")
                    speak(f"I successfully made {name} folder.")
                else:
                    raise Exception("sorry")
            except Exception as e:
                print("Nina: Sorry, I am not able to make new folder.")
                speak("Sorry, I am not able to make new folder.")
        elif 'play game' in query:
            print("Nina: Which game you want to play?")
            speak("Which game you want to play?")
            game = takeCommand().lower()
            try:
                if game != "none":
                    if game == "ghost":
                        print(f"Opening {game} game...")
                        os.startfile("C:\\Users\\dola\\Desktop\\computer\\game.html")
                    elif game == "snake":
                        print(f"Opening {game} game...")
                        os.startfile("C:\\Users\\dola\\Desktop\\computer\\Snake game\\index.html")
                    else:
                        print(f"Nina: No {game} game found!!")
                        speak(f"No {game} game found!!")
                else:
                    raise Exception("Sorry")
            except Exception as e:
                print("Nina: Sorry, I am not able to open your game")
                speak("Sorry, I am not able to open your game")
        elif 'exit' in query or 'quit' in query:
            print("Nina: You exited")
            exit()
