artilharia = list()

while True:
    jogador = dict()

    print("-"*30)
    jogador['nome'] = str(input('Nome do Jogador: '))
    gols = list()
    total = 0
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for i in range(partidas):
        valor = int(input(f'Quantos gols na partida {i+1}? '))
        gols.append(valor)
        total = total + valor

    jogador['gols'] = gols[:]
    jogador['total'] = total

    artilharia.append(jogador.copy())

    cont = str(input('Quer continuar? [S/N] '))
    if cont in "Nn":
        break

print("-"*30)

print("COD NOME           GOALS           TOTAL")
print('-'*30)
for i in range(len(artilharia)):
    print("{:< 4d}".format(i+1) + "{:< 15d}".format(artilharia[i]['nome'])
          + "{:<16d}".format(artilharia[i]['gols']) + "{:<5d}".format(artilharia[i]['total']))

while True:
    print("-"*30)
    num = int(input("Mostrar dados de qual jogador? "))
    if num == 999:
        print("<< VOLTE SEMPRE >>")
        break
    elif num > len(artilharia):
        print(f"ERRO! Não existe jogador com o código {num}! Tente novamente.")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {artilharia[num-1]['nome']}:")
        jogo = 1
        for j in artilharia[num-1]['gols']:
            print(f"No jogo {jogo} fez {j} gols.")

