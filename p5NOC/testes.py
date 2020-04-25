import numpy as np
'''
x1 = np.arange(9.0).reshape((3,3))
x2 = np.arange(3.0)

print(x1)
print(x2)

print(np.add(x1, x2))


n1 = 45
n2 = 50

v1 = np.array([n1,n2])


p1 = np.multiply(v1, 0.5)

print(v1)
print(v1[0])
print(p1)
'''

n1 = 3
n2 = 4
print(f'Vetor: ({n1},{n2})')
v1 = np.array([n1,n2])
mag = np.linalg.norm(v1)
print(f'Magnitude: {mag}')
limite = 4.5
print(f'O limite é {limite}')
n3 = n1 * limite / mag
n4 = n2 * limite / mag
print(f'Vetor Novo: ({n3},{n4})')
v2 = np.array([n3,n4])
mag2 = np.linalg.norm(v2)
print(f'Magnitude Nova : {mag2}')





#np.linalg.norm(vector)