from gtts import gTTS
import os
from pygame import mixer
import time




def speak_text(txt, dest):
        mixer.init()
        tts = gTTS(text=txt, lang=dest)
        tts.save("output.mp3")
        mixer.music.load("output.mp3")
        mixer.music.play()
        time.sleep(4)
        os.remove("output.mp3")
