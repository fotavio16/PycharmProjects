from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot("Bot")
bot.set_trainer(ListTrainer)

dir = os.getcwd() + "/portuguese"

for arqs in os.listdir(dir):
    print(f'Treinamento de {arqs}.')
    path = dir + "/" + arqs
    dados = open(path, 'r').readlines()
    #print(dados[0:100])
    bot.train(dados)

#with open('C:/path/numbers.txt') as f:
#    lines = f.read().splitlines()


while True:
    msg = input("Você: ")
    if msg.strip() != 'Bye':
        reply = bot.get_response(msg)
        print("ChatBot: ",reply)

    if msg.strip() == 'Bye':
        print("ChatBot: Bye")
        break
