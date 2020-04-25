def media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4)/4

def area_circ(r):
    return PI * r**2

def perim_circ(r):
    return 2 * PI * r

nota1 = 9
nota2 = 7
nota3 = 8.2
nota4 = 9.6

print(f'A média das notas é {media(nota1,nota2,nota3,nota4)}.')

PI = 3.141592
raio = 2.5

print(f'O círculo de raio {raio} tem perímetro de {perim_circ(raio)} e área de {area_circ(raio)}.')

