import pyttsx3
import datetime


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[7].id)
# Possible Voices
# 10 7 28 26 25

newVoiceRate = 190  # defalult voice rate 200
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = str(datetime.datetime.now().day)
    speak("Today is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back Sir!")
    time()
    speak("Friday at your service Sir!")


wishme()
