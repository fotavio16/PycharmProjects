def programa1():
    '''
        Faça um Programa que leia três números e mostre o
        maior deles.
    '''

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))

    if num1 > num2:
        maior = num1
    else:
        maior = num2
    if num3 > maior:
        maior = num3

    print(f'O maior dos três número é {maior}.')

def programa2():
    '''
        Faça um Programa que verifique se uma letra digitada
        é F ou M. Conforme a letra escrever: F - Feminino,
        M - Masculino, Sexo Inválido.
    '''

    letra = str(input("Digite o sexo (F/M): ")).upper()

    if letra == 'F':
        print("Sexo: F - Feminino")
    elif letra == 'M':
        print("Sexo: M - Masculino")
    else:
        print("Sexo inválido")

def programa3():
    '''
    Tendo como dados de entrada a altura e o sexo e peso
    de uma pessoa, construa um algoritmo que calcule seu peso
    ideal e informe se ela está dentro, acima ou abaixo do
    peso, utilizando as seguintes fórmulas:
    Para homens: (72.7 * h) - 58;
    Para mulheres: (62.1 * h) - 44.7
    :return:
    '''

    sexo = str(input("Qual o seu sexo (M/F)? ")).upper()
    altura = float(input("Qual a sua altura em centímetro? "))
    peso = float(input("Qual o seu peso em kilogramas? "))

    if sexo == 'M':
        pesoideal = altura * 72.7 / 100 - 58
    else:
        pesoideal = altura * 62.1 / 100 - 44.7

    if peso == pesoideal:
        print("Você está no peso ideal.")
    elif peso < pesoideal:
        print("Você está abaixo do peso ideal.")
    else:
        print("Você está acima do peso ideal.")


def programa4():
    '''
        Faça um Programa que pergunte em que turno você estuda.
        Peça para digitar M-matutino ou V-Vespertino ou
        N- Noturno. Imprima a mensagem Bom Dia!, Boa Tarde! ou
        Boa Noite! ou Valor Inválido!, conforme o caso.
    :return:
    '''

    print("Qual turno você estudo?")
    turno = str(input("M-matutino ou V-Vespertino ou N-Noturno: ")).upper()[0]

    if turno == 'V':
        print("Boa Tarde!")
    elif turno == 'M':
        print("Bom Dia!")
    elif turno == 'N':
        print("Boa Noite!")
    else:
        print("Valor inválido!")


def programa5():
    '''
    Faça um programa que faça 5 perguntas para uma pessoa
    sobre um crime:
    Telefonou para a vítima?,
    Esteve no local do crime?,
    Mora perto da vítima?,
    Devia para a vítima? e
    Já trabalhou com a vítima?
    O programa deve no final emitir uma classificação sobre
    a participação da pessoa no crime. Se a pessoa responder
    positivamente a 2 questões ela deve ser classificada como
    Suspeita, entre 3 e 4 como Cúmplice e 5 como Assassino.
    Caso contrário, ele será classicado como Inocente.
    :return:
    '''

    respondeuSIM = 0
    print("Responda as questões.")
    p1 = str(input("Telefonou para a vítima (S/N)? ")).upper()[0]
    if p1 == 'S':
        respondeuSIM += 1
    p2 = str(input("Esteve no local do crime (S/N)? ")).upper()[0]
    if p2 == 'S':
        respondeuSIM += 1
    p3 = str(input("Mora perto da vítima (S/N)? ")).upper()[0]
    if p3 == 'S':
        respondeuSIM += 1
    p4 = str(input("Devia para a vítima (S/N)? ")).upper()[0]
    if p4 == 'S':
        respondeuSIM += 1
    p5 = str(input("Já trabalhou com a vítima (S/N)? ")).upper()[0]
    if p5 == 'S':
        respondeuSIM += 1

    if respondeuSIM < 2:
        print("É inocente.")
    elif respondeuSIM == 2:
        print("É Suspeito.")
    elif respondeuSIM == 5:
        print("É o Assassino!")
    else:
        print("É um cúmplice.")


def programa6():
    '''
        Faça um programa que peça uma nota, entre zero e dez.
        Mostre uma mensagem caso o valor seja inválido e
        continue pedindo até que o usuário informe um valor válido.

    '''

    print("Digite uma nota entre 0 e 10:")

    while True:
        nota = int(input())
        if nota < 0 or nota > 10:
            print("Você digitou uma nota inválida. Digite novamente: ")
        else:
            break

    print(f'A nota foi {nota}.')

def programa7():
    '''
    Faça um programa que leia um nome de usuário e a sua senha
    e não aceite a senha igual ao nome do usuário, mostrando
    uma mensagem de erro e voltando a pedir as informações.
    :return:
    '''

    nome = str(input("Digite o nome do usuário: "))

    while True:
        senha = str(input("Digite a senha: "))
        if nome == senha:
            print("ERRO. A senha não pode ser igual ao número.")
        else:
            print("Nome e Senha cadastrados com sucesso.")
            break

programa7()

