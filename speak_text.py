from gtts import gTTS
import os
import pygame

def speak_text(txt, dest):
        pygame.init()
        tts = gTTS(text=txt, lang=dest)
        tts.save("output.mp3")
        sound = pygame.mixer.Sound("output.mp3")
        sound.play()
        os.remove("output.mp3")
