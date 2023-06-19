from gtts import gTTS
import os
import pygame.mixer
import pygame
from pygame import mixer

pygame.mixer.init(44100, -16,2,2048)



def speak_text(txt, dest):
        tts = gTTS(text=txt, lang=dest)
        tts.save("output.mp3")
        sound = mixer.Sound("output.mp3")
        sound.play()
        os.remove("output.mp3")
