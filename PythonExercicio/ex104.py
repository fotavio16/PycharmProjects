from termcolor import colored

def leiaInt(texto):
    print('-' * 30)
    while True:
        num = input(texto)
        if num.isdigit():
            break
        print(colored('ERRO! Digite um número inteiro válido.','red', 'on_yellow'))
    return num


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Vaocê acabou de digitar o número {n}')