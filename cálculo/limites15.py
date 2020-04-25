'''
    Limites - Finding Limits Numerically Using a Table - 02
    e(x)={  5,      if x=0
            1+x**2,   otherwise
 '''

import pandas as pd

def f(x):
    if x == 0:
        return 5
    else:
        return 1 + x**2


# Cria o dataframe com uma coluna dos valores de x
x = [-1, -0.5, -0.2, -0.1, -0.01, 0, 0.01, 0.1, 0.2, 0.5, 1]
y = [f(i) for i in x]
df = pd.DataFrame({' x':x, 'f(x)': y})

# Mostra o dataframe
print(df)