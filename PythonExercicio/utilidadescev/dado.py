def leiaDinheiro(texto):
    while True:
        valor = str(input(texto))
        valor = valor.replace(',', '.')
        valor = valor.strip()
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO: \"{valor}\" é um preço inválido!\033[m')
        else:
            return float(valor)

def leiaInt(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            return int(num)
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
