# Função que escreve formatado
def escreva(texto):
    tam = len(texto) + 4
    print('~' * tam)
    print(f'  {texto}')
    print('~' * tam)


# Programa Principal
escreva("Olá, Mundo!")
escreva("Fernando Otávio Gomes da Fonseca")
escreva("Azul")