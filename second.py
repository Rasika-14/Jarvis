#from tkinter import *
import datetime
from tkinter import Button

from tinker import Tk
import pyttsx3

from tinker import window

root = Tk()
root.title("First try")
root.geometry("800x500")


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
newVoiceRate = 200
engine.setProperty('rate', newVoiceRate)


# def talk():
#     engine.runAndWait()
#     my_entry.delete(0,END)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


# my_entry = Entry(root, font=("Helvetica", 28))
# my_entry.pack(pady=20)

# l1=Label(window,text="Time")
# l1.grid(row=1,column=0)

my_button = Button(root, text="Speak", command=time)
my_button.pack(pady=20)

root.mainloop()