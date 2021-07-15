from math import e
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
from wikipedia.wikipedia import search, summary
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
newVoiceRate = 200
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back!")
    speak("Jarvis at your service. How can I help you?")


def takeCommand():
    r = sr.Recognizer()
    my_mic_device = sr.Microphone(device_index=1)
    with my_mic_device as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio)
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again....")

        return "None"

    return query


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("","")
    server.sendmail("", to, content)
    server.close()


def screenshot():
    speak("Please tell me the name for this screenshot file")
    name = takeCommand().lower()
    speak("Please hold the screen for few second , I am taking screenshot")
    img = pyautogui.screenshot()
    img.save(f"E://images//{name}.png")
    speak("I take a screenshot")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


def jockes():
    speak(pyjokes.get_joke())


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
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I send ?")
                content = takeCommand()
                to = "xyz@gmail.com"
                #sendmail(to, content)
                speak(content)
            except Exception as e:
                speak(e)
                speak("Unable to send mail")
        elif "search in chrome" in query:
            speak("What should I search ?")
            chromepath = "C://Program Files//Google//Chrome//Application//chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        # elif "play songs" in query:
        #     songs_dir = "D:\a"
        #     songs = os.listdir(songs_dir)
        #     os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remember that" in query:
            speak("What should I remember ?")
            data = takeCommand()
            speak("You said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that" + remember.read())
        elif "screenshot" in query:
            screenshot()
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jockes()