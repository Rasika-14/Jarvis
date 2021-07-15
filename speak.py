import pyttsx3
import speech_recognition as sr
import pyaudio


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
newVoiceRate = 200
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    speak("Welcome back!")
    speak("Jarvis at your service. How can I help you?")

wishme()

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

takeCommand()