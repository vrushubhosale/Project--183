from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess

root = Tk()
root.geometry("500x500")
root.config(background = "orange")

label =Label(root, text="WELCOME TO YS&SB DESKTOP ASSISTANT",bg="orange")
label.place(relx=0.5,rely=0.1,anchor=CENTER)

text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speech_recognition= sr.Recognizer()
    speak("How may i help you?")
    with sr.Microphone() as source:
        audio= speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data= speech_recognisor.recognize_google(audio, language='en-us')
        except:
            print('please repeat i did not get that')
            speak('please repeat i did not get that')
        respond(voice_data)
        
def respond(voice_data):
    print(voice_data)
    if "name" in voice_data:
        speak("My name is YS&SB Desktop assistant")
        print("My name is YS&SB Desktop assistant")
        
    if "time" in voice_data:
        speak("Current time is : ")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
    if "search" in voice_data:
        speak("OPENING THE BEST SEARCH ENGINE OF ALL TIME")
        print("OPENING THE BEST SEARCH ENGINE OF ALL TIME")
        webbrowser.get().open("https://search.brave.com/")
        
    if "video" in voice_data:
        speak("OPENING THE BEST BEST VIDEO ENTERTAINMENT TOOL OF ALL TIME")
        print("OPENING THE BEST BEST VIDEO ENTERTAINMENT TOOL OF ALL TIME")
        webbrowser.get().open("https://www.bing.com/videos/")
        
    if "settings" in voice_data:
        speak("Opening your system settings")
        print("OPENING THE BEST SETTINGS")
        subprocess.Popen(["settings.exe"])
        
btn= Button(root, text="Begin",bg="red3", fg="white", padx=10, pady=1, relief=FLAT, command=r_audio)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()        