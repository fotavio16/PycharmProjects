# Linear Regression

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

# Cria o dataset para uso
diabetes = load_diabetes()
print(diabetes.data.shape)
# Será utilizada uma característica
diabetes_X = diabetes.data[:, None, 2]

# Cria a instânica da LinearRegression
LinRegT = LinearRegression()
LinReg = LinearRegression()

# Cria os conjuntos de treinamento e teste
X_trainset, X_testset, y_trainset, y_testset = train_test_split(diabetes_X, diabetes.target, test_size=0.3, random_state=7)

# Treina a rede
LinRegT.fit(diabetes_X,diabetes.target)
LinReg.fit(X_trainset,y_trainset)

# Plota o resultado da predição
plt.scatter(diabetes_X, diabetes.target,  color='black')
plt.scatter(X_testset, y_testset, color='red')
plt.plot(diabetes_X, LinRegT.predict(diabetes_X), color='green', linewidth=3)
plt.plot(X_testset, LinReg.predict(X_testset),color='blue', linewidth=3)
plt.show()


