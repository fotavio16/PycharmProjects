# Regression Evaluation Metrics

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
import numpy as np

# Cria o dataset para uso
diabetes = load_diabetes()

# Será utilizada uma característica
diabetes_X = diabetes.data[:, None, 2]

# Cria a instânica da LinearRegression
LinReg = LinearRegression()

# Cria os conjuntos de treinamento e teste
X_trainset, X_testset, y_trainset, y_testset = train_test_split(diabetes_X, diabetes.target, test_size=0.3, random_state=7)

# Treina a rede
LinReg.fit(X_trainset,y_trainset)

# Calcula o erro médio
print("Erro médio = {}.".format(np.mean(abs(LinReg.predict(X_testset) - y_testset))))

# Calcula o erro quadrático médio
print("Erro Quadrático médio = {}.".format(np.mean((LinReg.predict(X_testset) - y_testset) ** 2)))

# Calcula o erro quadrático médio
print("Raiz quadrada do Erro Quadrático médio = {}.".format(np.mean((LinReg.predict(X_testset) - y_testset) ** 2) ** (0.5) ))

