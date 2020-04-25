from termcolor import colored

def leiaInt(texto):
    print('-' * 30)
    while True:
        try:
            num = int(input(texto))
        except (ValueError, TypeError):
            print('Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar o dado.')
        else:
            print(f'Você acabou de digitar o número {num}')
            break
    return num

def leiaFloat(texto):
    print('-' * 30)
    while True:
        try:
            num = float(input(texto))
        except (ValueError, TypeError):
            print('Digite um número válido.')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar o dado.')
        else:
            print(f'Você acabou de digitar o número {num}')
            break
    return num

# Programa Principal
n = leiaInt('Digite um número: ')
p = leiaFloat('Digite um número com decimais: ')