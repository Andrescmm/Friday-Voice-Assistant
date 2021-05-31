import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[10].id)
# Possible Voices
# 10 7 28 26 25

newVoiceRate = 180  # defalult voice rate 200
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    speak("The current time is")
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
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 19 and hour <= 24:
        speak("Good Evening")
    else:
        speak("Good Nigth")
    speak("Friday at your service Sir!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source, timeout=2, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"

    return query


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("text@gmail,com", "test123")
    server.sendmail("text@gmail.com", to, content)
    server.close()


if __name__ == "__main__":

    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendmail(to, content)
                speak("Email send succesfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the email ")
