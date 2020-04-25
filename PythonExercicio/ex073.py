campeonato = ('Flamengo', 'Atlético-MG', 'São Paulo', 'Internacional', 'Grêmio',
              'Palmeiras', 'Sport', 'Cruzeiro', 'Botafogo', 'Corinthians', 'Vasco',
              'Fluminense', 'América-MG', 'Chapecoense', 'Santos', 'Vitória-BA',
              'Bahia', 'Paraná', 'Atlético-PR', 'Ceará')

print("CAMPEONATO BRASILEIRO DE 2018")
print()
print("Os 5 primeiros colocados são: ", end='')
for i in range(4):
    print(f'{campeonato[i]}, ', end='')
print(f'{campeonato[4]}.')
print()
print(f'Os 5 primeiros colocados são: {campeonato[:5]}')
print()
print("Os 4 últimos colocados são: ", end='')
for i in range(16,19):
    print(f'{campeonato[i]}, ', end='')
print(f'{campeonato[19]}.')
print()
print(f'Os 4 últimos colocados são: {campeonato[16:]}')
ordenada = sorted(campeonato)
print()
print('Lista dos times: ', end='')
for i in range(20):
    print(f'{ordenada[i]}, ', end='')
print()
print(f'Lista ordenada dos times: {ordenada}')
print(f'Lista ordenada dos times: {sorted(campeonato)}')
print()
pos = campeonato.index('Chapecoense') + 1
print(f'O Chapecoense está na posição {pos} do campeonato')
