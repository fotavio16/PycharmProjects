# Rede K-Nearest Neighbors

import numpy as np
import pandas
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

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


# Carrega o arquivo de dados na variável
my_data = pandas.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/HSAUR/skulls.csv", delimiter=",")

# Define a entrada com as colunas numérias
X = removeColumns(my_data, 0, 1)
# Define o objetivo
y = target(my_data, 1)
print(y)

# Cria os conjuntos de treinamento e teste para X e y
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=0)
#print(X_testset.shape)
#print(y_testset.shape)
print(y_testset)

# Define duas variáveis neigh e neigh7 para serem treinadas
neigh = KNeighborsClassifier(n_neighbors=1)
neigh23 = KNeighborsClassifier(n_neighbors=23)
neigh90 = KNeighborsClassifier(n_neighbors=90)

# Executa o treinamento
neigh.fit(X_trainset,y_trainset)
neigh23.fit(X_trainset,y_trainset)
neigh90.fit(X_trainset,y_trainset)

# Executa a predição nas amostras de teste
pred = neigh.predict(X_testset)
pred23 = neigh23.predict(X_testset)
pred90 = neigh90.predict(X_testset)

# Mostra a acuracidade
print("Acuracidade com um vizinho: {}".format(metrics.accuracy_score(y_testset, pred)))
print("Acuracidade com 23 vizinhos: {}".format(metrics.accuracy_score(y_testset, pred23)))
print("Acuracidade com 90 vizinhos: {}".format(metrics.accuracy_score(y_testset, pred90)))


