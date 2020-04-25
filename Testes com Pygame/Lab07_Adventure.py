from random import randint

# Cria a lista de Quartos
room_list = []
# O primeiro elemento é uma string com a descrição do quarto.
# Os últimos quatro elementos são o número da próxima sala
# se o usuário for para o norte, leste, sul ou oeste.
room = ['Você está em Dormitório 2. Existe uma passagem para Leste.', None, 1, None, None]
room_list.append(room)
room = ['Você está em Salão Sul. Existem passagens para Norte, Leste e Oeste.', 4, 2, None, 0]
room_list.append(room)
room = ['Você está em Sala de Jantar. Existe uma passagem para Oeste.', None, None, None, 1]
room_list.append(room)
room = ['Você está em Dormitório 1. Existe uma passagem para Leste.', None, 4, None, None]
room_list.append(room)
room = ['Você está em Salão Norte. Existem passagens para Norte, Leste, Sul e Oeste.', 6, 5, 1, 3]
room_list.append(room)
room = ['Você está em Cozinha. Existe uma passagem para Oeste.', None, None, None, 4]
room_list.append(room)
room = ['Você está em Varanda. Existe uma passagem para Sul.', None, None, 4, None]
room_list.append(room)

# Inicializa variáveis
current_room = randint(0,6)
done = False

# Loop Principal
while not done:

    print(f'\n{room_list[current_room][0]}')

    resp = str(input("Onde você quer ir? (N,S,L,O) ou Q para Sair: ")).upper()

    # Trata a direção que usuário optou
    if resp in "N":
        next_room = room_list[current_room][1]

    elif resp in "L":
        next_room = room_list[current_room][2]

    elif resp in "S":
        next_room = room_list[current_room][3]

    elif resp in "O":
        next_room = room_list[current_room][4]

    elif resp == "Q":
        done = True

    else:
        print("Desculpe. Não consigo entender o que você quer.")

    # Testa se o usuário escolheu uma saída possível
    if next_room == None:
        print("Desculpe, mas você não pode ir por esta.")
    else:
        current_room = next_room

print("FIM de JOGO. Obrigado.")