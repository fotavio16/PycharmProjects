# Regression Algorithms

from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

# Cria o dataset para uso
diabetes = load_diabetes()
# the categories are:
#        AGE SEX BMI (Body Mass Index)
#        BP (Blood Pressure)
#        Serum Measurements (6 blood serum measurements).

# Vamos usar a feature BMI (Body Mass Index)
diabetes_X = diabetes.data[:, None, 4]

# Cria a instânica da LinearRegression
LinReg = LinearRegression()

# Treina a rede com o conjunto de dados total
LinReg.fit(diabetes_X, diabetes.target)

# Plota o resultado da predição
plt.scatter(diabetes_X, diabetes.target,  color='black')
plt.plot(diabetes_X, LinReg.predict(diabetes_X), color='blue', linewidth=3)
plt.show()

