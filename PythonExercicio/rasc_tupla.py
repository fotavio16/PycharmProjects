lanche = ('Chedar', 'Batata Frita', 'Pizza', 'Suco de Uva', 'MilkShake')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

lanche = sorted(lanche)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi muito... muito... muito.')

a = (2,5,4)
b = (5,8,1,2)
c = b + a + a
print(f'Este é o c: {c}')
print(f'Quantos 5 tem? {c.count(5)}')
print(f'Qual a posição do primeiro 4? {c.index(4)}')