# Regressão Linear

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

# Faz a carga do dataset na variável
diabetes = load_diabetes()

# Vamos trabalhar com uma característica (coluna) do dataset
diabetes_X = diabetes.data[:, None, 2]
#print(diabetes_X)

# Cria a instânica da LinearRegression
LinReg = LinearRegression()

# Cria os conjuntos de treinamento e teste
X_trainset, X_testset, y_trainset, y_testset = train_test_split(diabetes_X, diabetes.target, test_size=0.3, random_state=7)
#print(X_testset.shape)
#print(y_testset.shape)
#print(y_testset)

# Treina a rede
LinReg.fit(X_trainset,y_trainset)

# Plota o resultado da predição
plt.scatter(X_testset, y_testset, color='black')
plt.plot(X_testset, LinReg.predict(X_testset),color='blue', linewidth=3)
plt.show()
