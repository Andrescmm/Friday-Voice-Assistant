import pyttsx3
import datetime


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[7].id)
# Possible Voices
# 10 7 28 26 25

newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak("At your servive sir, Welcome home")
