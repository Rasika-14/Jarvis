import pyttsx3
import datetime


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
newVoiceRate = 200
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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


wishme()
date()

# def takeCommand():
#     r = sr.Recognizer()
#     my_mic_device = sr.Microphone(device_index=1)
#     with my_mic_device as source:
#         print("Listening...")
#         r.adjust_for_ambient_noise(source)
#         r.pause_threshold = 1
#         audio = r.listen(source)
#
#     try:
#         print("Recognizing")
#         query = r.recognize_google(audio)
#         print(query)
#
#     except Exception as e:
#         print(e)
#         speak("Say that again....")
#
#         return "None"
#
#     return query
#
#
#
# if __name__ == "__main__":
#
#     wishme()
#
#     while True:
#         query = takeCommand().lower()
#         print(query)
#
#         if "time" in query:
#             time()
#         elif "date" in query:
#             date()
#         elif "offline" in query:
#             quit()
#