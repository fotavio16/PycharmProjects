import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

# Define uma função que calcula o erro na aproximação theta
def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))

# Define a Função de Gradiente Descent
def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    #print(temp)
    parameters = int(theta.ravel().shape[1])
    #print(parameters)
    cost = np.zeros(iters)
    #print(cost)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:,j])
            temp[0,j] = theta[0,j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta, cost

path = os.getcwd() + '\data\ex1data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])

#print(data.head())
#print(data.describe())

#data.plot(kind='scatter', x='Population', y='Profit', figsize=(12,8))

# Acrescenta uma coluna de 1s na frente dos dados
data.insert(0, 'Ones', 1)
#print(data.head())

# Define X (dados de treinamento) e y (objetivo)
cols = data.shape[1]
X = data.iloc[:,0:cols-1]
y = data.iloc[:,cols-1:cols]
#print(cols)
#print(X)
#print(y)

# Converte os frames de dados para matrizes numpy
X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0,0]))
#print(X)
#print(y)
#print(theta)

#print(computeCost(X, y, theta))

# Inicializa as variáveis de learning rate e número de iterações
alpha = 0.01
iters = 1000

# Executa o gradiente descent para adequar ao modelo de parâmetros
g, cost = gradientDescent(X, y, theta, alpha, iters)
print(g) # Novo theta calculado após as iterações
# print(cost)

# Plotando os resultados
x = np.linspace(data.Population.min(), data.Population.max(), 100)
f = g[0, 0] + (g[0, 1] * x)

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(data.Population, data.Profit, label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')

fig1, ax1 = plt.subplots(figsize=(12,8))
ax1.plot(np.arange(iters), cost, 'r')
ax1.set_xlabel('Iterations')
ax1.set_ylabel('Cost')
ax1.set_title('Error vs. Training Epoch')

plt.show()
