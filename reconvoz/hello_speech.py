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

speak('hello Brazil')

falar('Olá, Brasil. Boa tarde.')
