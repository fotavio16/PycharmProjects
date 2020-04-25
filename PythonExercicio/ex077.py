palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for p in palavras:
    print(f'Na palavra {p} temos ', end='')
    p = p.lower()
    for car in p:
        if car in ('a', 'e', 'i', 'o', 'u'):
            print(f'{car} ', end='')
    print()
