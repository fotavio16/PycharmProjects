def ficha(nome='Indefinido',num=0):
    print(f'O jogador {nome} fez {num} gol(s) no campeonato.')


# Programa Principal
print('-' *30)
jogador = str(input('Nome do Jogador: '))
gols = int(input('Número de Gols: '))
ficha(jogador,gols)