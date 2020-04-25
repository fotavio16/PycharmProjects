import numpy as np
import pandas
from sklearn.neighbors import KNeighborsClassifier

def removeColumns(pandasArray, *column):
    return pandasArray.drop(pandasArray.columns[[column]], axis=1).values

def targetAndtargetNames(numpyArray, targetColumnIndex):
    target_dict = dict()
    target = list()
    target_names = list()
    count = -1
    for i in range(len(my_data.values)):
        if my_data.values[i][targetColumnIndex] not in target_dict:
            count += 1
            target_dict[my_data.values[i][targetColumnIndex]] = count
        target.append(target_dict[my_data.values[i][targetColumnIndex]])
    # Since a dictionary is not ordered, we need to order it and output it to a list so the
    # target names will match the target.
    for targetName in sorted(target_dict, key=target_dict.get):
        target_names.append(targetName)
    return np.asarray(target), target_names


# Salva na variável o arquivo panda skulls.csv
my_data = pandas.read_csv("skulls.csv", delimiter=",")

#print(type(my_data))
#print(my_data)
print(my_data.columns)
#print(my_data.values)
print(my_data.shape)

new_data = removeColumns(my_data, 0, 1)
#print(new_data)

target, target_names = targetAndtargetNames(my_data.values, 0)
#print(target, target_names)

X = new_data
y = target
neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(X,y)
print('Prediction: {}'.format(neigh.predict(new_data[50])))
print('Actual: {}'.format(y[50]))

