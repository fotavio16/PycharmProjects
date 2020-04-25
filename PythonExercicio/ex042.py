print('Teste dos lados de um triângulo:')
lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))
if lado1 > lado2 + lado3 or lado3 > lado2 + lado1 or lado2 > lado1 + lado3:
    print('As dimensões informadas não formam um triângulo.')
elif lado1**2 == lado3**2 + lado2**2 or lado2**2 == lado3**2 + lado1**2 or lado3**2 == lado1**2 + lado2**2:
    print('Este é um triângulo retângulo.')
elif lado1 == lado2 and lado1 == lado3:
    print('Este é um triângulo equilátero.')
elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
    print('Este é um triângulo isósceles.')
else:
    print('Este é um triângulo escaleno.')
