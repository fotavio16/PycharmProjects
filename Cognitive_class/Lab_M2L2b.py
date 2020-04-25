# Decision Trees

import numpy as np
import pandas
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# Remove the column containing the target name since it doesn't contain numeric values.
# Also remove the column that contains the row number
# axis=1 means we are removing columns instead of rows.
# Function takes in a pandas array and column numbers and returns a numpy array without
# the stated columns
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

def getFeatureNames(pandasArray, *column):
    actualColumns = list()
    allColumns = list(pandasArray.columns.values)
    for i in sorted(column):
        actualColumns.append(allColumns[i])
    return actualColumns


# Carrega o arquivo de dados na variável
my_data = pandas.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/HSAUR/skulls.csv", delimiter=",")

# Define as variáveis de entrada e objetivo
X = removeColumns(my_data, 0, 1)
y, targetNames = targetAndtargetNames(my_data, 1)
featureNames = getFeatureNames(my_data, 2,3,4,5)
#print(y)
#print(targetNames)
#print(featureNames)

# Cria os conjuntos de treinamento e teste para X e y
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)
#print(X_testset.shape)
#print(y_testset.shape)

# Cria a rede DecisionTree
skullsTree = DecisionTreeClassifier(criterion="entropy")

# Treina a rede
skullsTree.fit(X_trainset,y_trainset)

# Testa as previsões
predTree = skullsTree.predict(X_testset)
print(predTree)
print(y_testset)

print("Precisão da Árvore de Decisão: {}".format(metrics.accuracy_score(y_testset,predTree)))


'''
from IPython.display import Image
from sklearn.externals.six import StringIO
from sklearn import tree
import pydot

dot_data = StringIO()

# Add in your code below
tree.export_graphviz(skullsTree, out_file=dot_data,
feature_names=featureNames,
class_names=targetNames,
filled=True, rounded=True,
special_characters=True,
leaves_parallel=True)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
Image(graph.)
'''
