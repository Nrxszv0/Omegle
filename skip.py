import os
import time
import playsound 
import speech_recognition as sr 
from gtts import gTTS

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

kbd = KeyboardController()
mse = MouseController()

def speak(text):
    tts = gTTS(text = text, lang="en") #transform text to audio file in english
    fileName = text + "voice.mp3" #save then paly file
    tts.save(fileName)
    playsound.playsound(fileName)

def get_audio():
    #return what we say into microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

# speak("hello")
# get_audio()
while True:

    text = get_audio()

    if "python skip" in text:
        mse.position = (500,500)
        time.sleep(0.01)
        mse.click(Button.left,1)
        
        time.sleep(0.01)
        kbd.press(Key.esc)
        time.sleep(0.02)    
        kbd.release(Key.esc)
        # speak("Skipping this bitch")

    if "python new chat" in text:
        mse.position = (500,500)
        time.sleep(0.01)
        mse.click(Button.left,1)
        
        time.sleep(0.01)
        kbd.press(Key.esc)
        time.sleep(0.02)    
        kbd.release(Key.esc)

        time.sleep(0.1)
        kbd.press(Key.esc)
        time.sleep(0.02)    
        kbd.release(Key.esc)

        time.sleep(0.1)
        kbd.press(Key.esc)
        time.sleep(0.02)    
        kbd.release(Key.esc)
        # speak("Skipping this bitch")
    if "quit program" in text:
        break

   
    

