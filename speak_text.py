from gtts import gTTS
import os
import pygame.mixer
import pygame

pygame.init()


def speak_text(txt, dest):
        tts = gTTS(text=txt, lang=dest)
        tts.save("output.mp3")
        sound = pygame.mixer.Sound("output.mp3")
        sound.play()
        os.remove("output.mp3")
