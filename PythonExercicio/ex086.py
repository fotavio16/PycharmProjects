grade = [[],[],[]]
for i in range(3):
    for j in range(3):
        grade[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

print('-='*30)
somaPares = 0
somaColuna3 = 0
maiorLinha2 = 0
for i in range(3):
    for j in range(3):
        print(f'[  {grade[i][j]}  ]',end='')
        if grade[i][j]%2 == 0:
            somaPares += grade[i][j]
        if j == 2:
            somaColuna3 += grade[i][j]
        if i == 1:
            if grade[i][j] > maiorLinha2:
                maiorLinha2 = grade[i][j]
    print()
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaColuna3}.')
print(f'O maior valor da segunda linha é {maiorLinha2}.')
