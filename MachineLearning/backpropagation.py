# Machine Learning, Neural Netwoks
# Classification, prediction
# Exemplo1 : Entradas : Horas de Estudo, Horas de Sono
#            Saída : Nota da prova
# Exemplo2 : Função XOR

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import TanhLayer

# Entradas e Saída esperada - Exemplo 1
# Cria o dataset
ds1 = SupervisedDataSet(2, 1)

# Adiciona as amostras
ds1.addSample((0.8, 0.4), (0.7)) # Valores normalizados entre 0 e 1
ds1.addSample((0.5, 0.7), (0.5))
ds1.addSample((0.99, 0.8), (0.95))

# Entradas e Saída esperada - Exemplo 1
# Cria o dataset
ds2 = SupervisedDataSet(2, 1)

# Adiciona as amostras
ds2.addSample((0, 0), (0))
ds2.addSample((0, 1), (1))
ds2.addSample((1, 0), (1))
ds2.addSample((1, 1), (0))

# Monta a rede 1 com 2 neurônios na entrada, 4 na camada oculta e 1 neurônio na saída
net1 = buildNetwork(2, 4, 1, bias=True)

# Monta a rede 2 com 2 neurônios na entrada, 3 na camada oculta e 1 neurônio na saída
net2 = buildNetwork(2, 3, 1, bias=True,  hiddenclass=TanhLayer)

# Conecta a rede e o dataset no treinamento
trainer1 = BackpropTrainer(net1, ds1)
trainer2 = BackpropTrainer(net2, ds2)

print("Iniciando o Treinamento da Rede 1")
erro = 10
epocas = 0
while erro > 0.01:
    erro = trainer2.train()
    epocas += 1
    print("Epoca {} - erro: {}.".format(epocas, erro))

print("\n")

print("Entrada (1,0) - saída {}.".format(net2.activate((1,0))))
print("Entrada (0,1) - saída {}.".format(net2.activate((0,1))))
print("Entrada (0,0) - saída {}.".format(net2.activate((0,0))))
print("Entrada (1,1) - saída {}.".format(net2.activate((1,1))))


while True:
    dormiu = float(input("Dormiu\n"))
    estudou = float(input("Estudou\n"))

    z = net1.activate((dormiu, estudou))[0] * 10.0

    print("A Previsão de nota é {}".format(str(z)))
