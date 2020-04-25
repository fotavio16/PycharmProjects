jogador = dict()

jogador['nome'] = str(input('Nome do Jogador: '))
gols = list()
total = 0
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for i in range(partidas):
    valor = int(input(f'Quantos gols na partida {i+1}? '))
    gols.append(valor)
    total = total + valor

jogador['gols'] = gols
jogador['total'] = total

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}.")

print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range(partidas):
    print(f"    => Na partida {i+1}, fez {jogador['gols'][i]} gols.")
print(f"Foi um total de {jogador['total']} gols.")
