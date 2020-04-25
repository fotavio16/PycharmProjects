import numpy as np
import pandas
from sklearn.neighbors import KNeighborsClassifier

# Remove the column containing the target name since it doesn't contain numeric values.
# Also remove the column that contains the row number
# axis=1 means we are removing columns instead of rows.
# Function takes in a pandas array and column numbers and returns a numpy array without
# the stated columns
def removeColumns(pandasArray, *column):
    return pandasArray.drop(pandasArray.columns[[column]], axis=1).values

def target(numpyArray, targetColumnIndex):
    target_dict = dict()
    target = list()
    count = -1
    for i in range(len(my_data.values)):
        if my_data.values[i][targetColumnIndex] not in target_dict:
            count += 1
            target_dict[my_data.values[i][targetColumnIndex]] = count
        target.append(target_dict[my_data.values[i][targetColumnIndex]])
    return np.asarray(target)


# Salva na variável o arquivo panda skulls.csv
my_data = pandas.read_csv("skulls.csv", delimiter=",")

# Define a entrada com as colunas numérias
X = removeColumns(my_data, 0, 1)
# Define o objetivo
# y = target(my_data.values, 0)
y = target(my_data, 1)

# Define duas variáveis neigh e neigh7 para serem treinadas
neigh = KNeighborsClassifier(n_neighbors=1)
neigh7 = KNeighborsClassifier(n_neighbors=7)
neigh.fit(X,y)
neigh7.fit(X,y)

# Visualização dos resultados para o 30º elemento
print('Prediction1: {}'.format(neigh.predict(X[50])))
print('Prediction7: {}'.format(neigh7.predict(X[50])))
print('Actual: {}'.format(y[50]))

