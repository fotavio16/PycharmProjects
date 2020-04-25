def programa1():
   '''
   Faça um programa (script) que peça dois números ao usuário
   e imprima a soma.
   :return:
   '''

   num1 = float(input("Digite um número: "))
   num2 = float(input("Digite o segundo número: "))
   soma = num1 + num2

   print(f'A soma dos números {num1} e {num2} é {soma}.')

def programa2():
    '''
        Faça um programa que peça um lado do quadrado,
        calcule a área, em seguida mostre o dobro desta
        área para o usuário.
    :return:
    '''

    lado = float(input("Digite o valor do lado do quadrado: "))
    area_quadrado = lado **2

    print(f'A área de um quadrado de lado {lado} é {area_quadrado}.')
    print(f'O dobro desta área é {area_quadrado*2}.')

def programa3():
    '''
        Faça um programa que peça a temperatura em graus
        Fahrenheit, transforme e mostre a temperatura em
        graus Celsius. (C = (5  (F
    :return:
    '''

    temp_Fahr = float(input("Digite a temperatura em Fahrenheit: "))
    temp_Celsius = 5 * (temp_Fahr - 32) / 9

    print(f'A temperatura em ºCelsius é {temp_Celsius}.')


def programa4():
    '''
        Faça um programa que peça 2 números inteiros e
        um número real. Calcule e mostre:
        (a) O produto do dobro do primeiro com metade do
        segundo .
        (b) A soma do triplo do primeiro com o terceiro.
        (c) O terceiro elevado ao cubo.
    :return:
    '''

    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    num3 = float(input("Digite um número real: "))

    print(f'O produto do dobro de {num1} pela metade de {num2} é {num1*num2}.')
    print(f'A soma do triplo de {num1} com {num3} é {3*num1 + num3}')
    print(f'{num3} elevado ao cubo é {num3**3}')


def programa5():
    '''
        Faça um programa que peça o tamanho de um arquivo
        para download (em MB) e a velocidade de um link de
        Internet (em Mbps), calcule e informe o tempo
        aproximado de download do arquivo usando este link
        (em minutos). Obs. 1 MB (megabyte) = 8 Mb(megabit).
    :return:
    '''

    tamanho = int(input("Digite o tamanho do arquivo em MB: "))
    velocidade = int(input("Digite a velocidade do link em Mbps: "))

    tempodwl = (tamanho * 8 / velocidade) / 60.0

    print(f'O tempo de download do arquivo é de {tempodwl} minutos.')

programa5()