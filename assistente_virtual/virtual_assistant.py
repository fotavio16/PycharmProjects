'''
    Descrição: Programa de Assistente Virtual que pega a data e hora atuais
                e responde com uma saudação randômica, e retorna informações
                sobre uma personalidade.
'''

# Importa as bibliotecas
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

# Ignora mensagens de aviso
warnings.filterwarnings('ignore')

# Record audio and return it as a string
def recordAudio():

    # Record the audio
    r = sr.Recognizer() # Creating a recognizer object

    # Open the microphone and star recording
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Diga algo!')
        audio = r.listen(source)

    # Use Google speech recognition
    data = ''
    try:
        data = r.recognize_google(audio, language='pt-BR')
        print(f'Você disse: {data}')
    except sr.UnknownValueError: # Check for unknown errors
        print('Google Speech Recognition could not understand the audio, unknown error.')
    except sr.RequestError as e:
        print(f'Request results from Google Speech Recognition service error {e}')

    return data

# Function to get the virtual assistant response
def assistantResponse(text):

    print(text)

    #Convert the text to speech
    #myobj = gTTS(text = text, lang='en', slow=False)
    myobj = gTTS(text=text, lang='pt-BR', slow=False)

    #Save converted audio to a file
    myobj.save('assist_resp.mp3')

    #Play the converted file
    os.system('start assist_resp.mp3')

# Function for wake word(s) or phrase
def wakeWord(text):

    WAKE_WORDS = ['hey computer', 'okay computer'] # List of wake words

    text = text.lower()

    #Check to see if the users command / text contains a wake word/phrase
    for frase in WAKE_WORDS:
        if frase in text:
            return True
    # Ao final do loop se não encontra a Wake Word retorna False
    return False

# Function to get the current date
def getDate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    # Lista de meses
    month_names = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                   'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    # Lista de ordinal numbers
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                      '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd',
                      '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    return f'Today is {weekday} {month_names[monthNum - 1]} the {ordinalNumbers[dayNum - 1]}.'

# Function to return a random greeting response
def greeting(text):

    # Greeting inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'wassup', 'hello']

    # Greeting responses
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']

    # If the users input is a greeting, the return a randomly chosen greeting response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) +'.'

    # If no greeting was detected then return an empty string
    return ''



#recordAudio()

#text = 'When the results came back positive, he decided to include it in his profile to attract reservations.'
text = 'Com a possibilidade de perder o vínculo com Marrony na Justiça, o Vasco colocou em dia tudo o que devia ao jogador.'
assistantResponse(text)
