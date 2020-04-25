print('Cálculo da nota final do aluno e sua situação.')
nota1 = float(input('Digite a nota 1 do aluno: '))
nota2 = float(input('Digite a nota 2 do aluno: '))
media = (nota1 + nota2) / 2
print("A nota final do aluno é {}.".format(media))
if media < 5:
    print("O aluno foi reprovado.")
elif media < 6.9:
    print("O aluno está em recuperação.")
else:
    print("O aluno está aprovado.")