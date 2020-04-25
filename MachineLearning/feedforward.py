# Machine Learning, Neural Netwoks
# Classification, prediction
# Exemplo : Função XOR

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import TanhLayer, LinearLayer, SigmoidLayer
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import RecurrentNetwork
from pybrain.structure import FullConnection # Permite a conexão de cada neurônio de uma camada com cada um da outra camada

# Entradas e Saída esperada - Exemplo 1
# Cria o dataset
ds1 = SupervisedDataSet(2, 1)

# Adiciona as amostras
ds1.addSample((0, 0), (0))
ds1.addSample((0, 1), (1))
ds1.addSample((1, 0), (1))
ds1.addSample((1, 1), (0))

# Monta a rede 1 com 2 neurônios na entrada, 4 na camada oculta e 1 neurônio na saída
net1 = buildNetwork(2, 4, 1, bias=True)

# Monta a rede 2 com 2 neurônios na entrada, 3 na camada oculta e 1 neurônio na saída
net2 = buildNetwork(2, 3, 1, bias=True,  hiddenclass=TanhLayer)

# Cria e configura a rede FeedForward
netFF = FeedForwardNetwork()
inLayer = LinearLayer(2) # 2 neurônios na entrada
hiddenLayer = SigmoidLayer(3) # 3 neurônios na camada oculta
outLayer = LinearLayer(1) # 1 neurônios na saída
netFF.addInputModule(inLayer)
netFF.addModule(hiddenLayer)
netFF.addOutputModule(outLayer)
# Cria as conexões entre as camadas
in_to_hidden = FullConnection(inLayer, hiddenLayer)
netFF.addConnection(in_to_hidden)
hidden_to_out = FullConnection(hiddenLayer, outLayer)
netFF.addConnection(hidden_to_out)
# Inicialização interna necessária permitir o usa da rede MLP
netFF.sortModules()

# Cria e configura a rede RecurrentNetwork
netRN = RecurrentNetwork()
netRN.addInputModule(LinearLayer(2, name='in'))
netRN.addModule(SigmoidLayer(3, name='hidden'))
netRN.addOutputModule(LinearLayer(1, name='out'))
netRN.addConnection(FullConnection(netRN['in'], netRN['hidden'], name='c1'))
netRN.addConnection(FullConnection(netRN['hidden'], netRN['out'], name='c2'))
netRN.addRecurrentConnection(FullConnection(netRN['hidden'], netRN['hidden'], name='c3'))
netRN.sortModules()

# Conecta a rede e o dataset no treinamento
trainer1 = BackpropTrainer(net1, ds1)
trainer2 = BackpropTrainer(net2, ds1)
trainer3 = BackpropTrainer(netFF, ds1)
trainer4 = BackpropTrainer(netRN, ds1)

# Começa o treinamento
erroMAX = 0.01

print("Iniciando o Treinamento da Rede 1...")
erro = 1
epocas = 0
while erro > erroMAX:
    epocas += 1
    erro = trainer1.train()
    # print("Epoca {} - erro: {}.".format(epocas, erro))
print("Treinamento da Rede 1 finalizado.")
print("Epocas: {}". format(epocas))
print("Erro: {}.".format(erro))
print("\n")

print("Iniciando o Treinamento da Rede 2...")
erro = 1
epocas = 0
while erro > erroMAX:
    epocas += 1
    erro = trainer2.train()
    # print("Epoca {} - erro: {}.".format(epocas, erro))
print("Treinamento da Rede 2 finalizado.")
print("Epocas: {}". format(epocas))
print("Erro: {}.".format(erro))
print("\n")

print("Iniciando o Treinamento da Rede 3 - FeedForward...")
erro = 1
epocas = 0
while erro > erroMAX:
    epocas += 1
    erro = trainer3.train()
    # print("Epoca {} - erro: {}.".format(epocas, erro))
print("Treinamento da Rede 3 - FeedForward finalizado.")
print("Epocas: {}". format(epocas))
print("Erro: {}.".format(erro))
print("\n")

print("Iniciando o Treinamento da Rede 4 - RecurrentNetwork...")
erro = 1
epocas = 0
while erro > erroMAX:
    epocas += 1
    erro = trainer4.train()
    # print("Epoca {} - erro: {}.".format(epocas, erro))
print("Treinamento da Rede 4 - RecurrentNetwork finalizado.")
print("Epocas: {}". format(epocas))
print("Erro: {}.".format(erro))
print("\n")

# Realiza testes com as redes
print("Testes com a Rede 1")
print("Entrada (1,0) - saída {}.".format(net1.activate((1,0))))
print("Entrada (0,1) - saída {}.".format(net1.activate((0,1))))
print("Entrada (0,0) - saída {}.".format(net1.activate((0,0))))
print("Entrada (1,1) - saída {}.".format(net1.activate((1,1))))
print("\n")

print("Testes com a Rede 2")
print("Entrada (1,0) - saída {}.".format(net2.activate((1,0))))
print("Entrada (0,1) - saída {}.".format(net2.activate((0,1))))
print("Entrada (0,0) - saída {}.".format(net2.activate((0,0))))
print("Entrada (1,1) - saída {}.".format(net2.activate((1,1))))
print("\n")

print("Testes com a Rede 3 - FeedForward")
print("Entrada (1,0) - saída {}.".format(netFF.activate((1,0))))
print("Entrada (0,1) - saída {}.".format(netFF.activate((0,1))))
print("Entrada (0,0) - saída {}.".format(netFF.activate((0,0))))
print("Entrada (1,1) - saída {}.".format(netFF.activate((1,1))))
print("\n")

print("Testes com a Rede 4 - RecurrentNetwork")
print("Entrada (1,0) - saída {}.".format(netRN.activate((1,0))))
print("Entrada (0,1) - saída {}.".format(netRN.activate((0,1))))
print("Entrada (0,0) - saída {}.".format(netRN.activate((0,0))))
print("Entrada (1,1) - saída {}.".format(netRN.activate((1,1))))
print("\n")
