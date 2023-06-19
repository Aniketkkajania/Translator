from gtts import gTTS


def speak_text(txt, dest):
        tts = gTTS(text=txt, lang=dest)
        tts.save("output.wav")