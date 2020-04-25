from gameobjects import Vector2

A = (10.0, 20.0)
B = (30.0, 35.0)
C = (15.0, 45.0)
AB = Vector2.from_points(A, B)
BC = Vector2.from_points(B, C)
print(f'Vector AB is {AB}')
print(f'AB * 2 is {AB * 2}')
print(f'AB / 2 is {AB / 2}')
#print(f'AB + (-10, 5) is {AB + (-10, 5)}')
print(f'Magnitude of AB is {AB.get_magnitude()}')
print(f'AB normalized is {AB.normalize()}')
print(f'Vector BC is {BC}')
AC = Vector2.from_points(A, C)
print(f'Vector AC is {AC}')
AC2 = AB + BC
print(f'But, AB + BC is {AC2}')

print()
step = AB * .1
position = Vector2(A[0], A[1])
for n in range(10):
    position += step
    print(f'Posição #{n}: {position}')
