import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


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
        audio = r.listen(source, timeout=20, phrase_time_limit=10)

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


def screenhot():
    img = pyautogui.screenshot()
    img.save("path")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + str(usage))

    battery = psutil.sensors_battery
    speak("Battery is at" + str(battery))


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":

    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        # time
        if "time" in query:
            time()

        # date
        elif "date" in query:
            date()

        # Offline
        elif "offline" in query:
            quit()

        # Wikipedia
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        # Email
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

        # PC commands
        elif "logout" in query:
            os.system("shutdown-1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        # Play a Song
        elif "play a song" in query:
            # song_dir = path ofthe songs
            #songs = os.listdir(song_dir)
            # os.startfile(os.path.join(songs_dir,songs[0]))
            speak("I'm sorry not avaliable right now")

        # Remember that
        elif "remember that" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("You said me to remember ")
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        # Do you know anything
        elif "Do you know anything?" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that " + remember.read())

        # Screenshot
        elif "Screenshot" in query:
            screenhot()
            speak("Done!")

        # cpu
        elif "cpu" in query:
            cpu()

        # Jokes
        elif "joke" in query:
            jokes()

        #Stop
        elif "Good bye" in query:
            break; 

