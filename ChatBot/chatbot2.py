from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Teste')
bot.set_trainer(ListTrainer)

conv1 = ['oi', 'olá', 'olá, bom dia.', 'bom dia',
         'bom dia, como vai?', 'estou bem']

bot.train(conv1)

while True:
    quest = input('Você: ')

    resposta = bot.get_response(quest)
    print(f'Bot: {resposta}')


