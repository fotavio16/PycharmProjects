from sklearn.datasets import load_digits # Importa a base de dados
from sklearn import svm # Importa a rede neural SVM

digits = load_digits()

# Mostrando os dados da base
print(type(digits))
print(digits.data)
print(digits.target)
print(digits.target_names)
print(digits.data.shape)
print(digits.target.shape)

# Aqui definimos as variáveis usadas no treinamento
X = digits.data
y = digits.target

# Define a rede neural e os parâmetros
clf = svm.SVC(gamma=0.001, C=100)
print()

# Executa o treinamento
clf.fit(X,y)

# Mostra o resultado
print('Prediction: {}'.format(clf.predict(digits.data[50])))
print('Actual: {}'.format(y[50]))

