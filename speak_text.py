from gtts import gTTS
import playsound
import os

def speak_text(txt, dest):
        tts = gTTS(text=txt, lang=dest)
        tts.save("output.mp3")
        playsound.playsound('output.mp3')
        os.remove('output.mp3')