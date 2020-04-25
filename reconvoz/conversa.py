import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def falar(texto):
    tts1 = gTTS(text=texto, lang='pt-br')
    arquivo = 'voz1.mp3'
    tts1.save(arquivo)
    playsound.playsound(arquivo)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""

    try:
        said = r.recognize_google(audio)
        print(said)
    except Exception as e:
        print("Exception: " + str(e))

    return said

def get_audio_file():
    aud_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ns004-01.wav")
    r = sr.Recognizer()

    with sr.AudioFile(aud_file) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        print(text)
    except:
        print("Não funciona.")


def ouvir_mic():
    rbr = sr.Recognizer()
    with sr.Microphone() as fonte:
        rbr.adjust_for_ambient_noise(fonte)
        audio = rbr.listen(fonte)
        fala = ""

        try:
            fala = rbr.recognize_google(audio, language='pt-BR')
            print(fala)
        except Exception as e:
            print("Exceção: " + str(e))

    return fala



#speak('hello everybody and welcome back')

#get_audio()

#falar("Olá. Diga alguma coisa.")

#ouvir_mic()

get_audio_file()


