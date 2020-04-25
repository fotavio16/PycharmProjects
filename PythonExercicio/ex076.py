produtos = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.9, 'Estojo', 25.0,
            'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32,
            'Canetas', 22.3, 'Livro', 34.9)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for i in range(0,len(produtos),2):
    print(f'{produtos[i]:.<30}'
          f'R${produtos[i+1]:>7.2F}')

print('-' * 40)