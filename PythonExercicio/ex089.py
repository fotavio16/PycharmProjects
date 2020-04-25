lista = []
while True:
    aluno = []
    nome = str(input('Nome: '))
    aluno.append(nome)
    notas = []
    for i in range(2):
        nno = float(input(f'Nota {i+1}: '))
        notas.append(nno)
    notas.append((notas[0]+notas[1]/2))
    aluno.append(notas[:])
    lista.append(aluno[:])
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'nN':
        break

print('-='*40)
print("No. NOME         MÉDIA")
print('-'*20)
for i in range(len(lista)):
    print("{:< 4d}".format(i) + "{:< 10d}".format(lista[i][0]) + "{:^6d}".format(lista[i][1][2]))

while True:
    print('-'*30)

    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if aluno == '999':
        break
    print(f'Notas de {lista[aluno][0]} são {lista[aluno][1][0:1]}')

print('FINALIZANDO....')
print('<<< VOLTE SEMPRE >>>')