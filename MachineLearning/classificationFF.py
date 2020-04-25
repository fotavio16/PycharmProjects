# Componentes necessários
# PyBrain
from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
# E demais módulos
from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal
import numpy as np

# Criação do dataset com um conjunto de pontos em 2D pertencentes a três classes diferentes
num_amostras = 1200
num_classes = 3
bounds = (0,1)
means = [(-1,0),(2,4),(3,1)]
cov = [diag([1,1]), diag([0.5,1.2]), diag([1.5,0.7])]
alldata = ClassificationDataSet(2, 1, nb_classes=3)

for n in range(int(num_amostras/num_classes)):
    for classe in range(num_classes):
        input = multivariate_normal(means[classe],cov[classe])
        alldata.addSample(input, [classe])

# Divide o dataset em treinamento 75% e teste 25%
tstdata, trndata = alldata.splitWithProportion( 0.25 )

# Codifica a saída (target) para um neurônio de saída por classe
# Para as amostras de treinamento
oldtarget = trndata.getField('target')
newtarget = np.zeros([len(trndata),num_classes], dtype='Int32')+bounds[0]
for i in range(len(trndata)):
    newtarget[i,int(oldtarget[i])] = bounds[1]
trndata.setField('class',oldtarget)
trndata.setField('target',newtarget)
# Para as amostras de teste
oldtarget = tstdata.getField('target')
newtarget = np.zeros([len(tstdata),num_classes], dtype='Int32')+bounds[0]
for i in range(len(tstdata)):
    newtarget[i,int(oldtarget[i])] = bounds[1]
tstdata.setField('class',oldtarget)
tstdata.setField('target',newtarget)

# Imprime algumas informações sobre os datasets
print ("Número de Amostras de Treinamento: ", len(trndata))
print ("Dimensões de Entrada e Saida: ", trndata.indim, trndata.outdim)
print ("Primeira Amostra (entrada, objetivo, classe):")
print (trndata['input'][0], trndata['target'][0], trndata['class'][0])

print ("Número de Amostras de Teste: ", len(tstdata))
print ("Dimensões de Entrada e Saida: ", tstdata.indim, tstdata.outdim)
print ("Primeira Amostra (entrada, objetivo, classe):")
print (tstdata['input'][0], tstdata['target'][0], tstdata['class'][0])

# Monta a rede com 5 neurônis na camada oculta
ffnet = buildNetwork(trndata.indim, 5, trndata.outdim, outclass=SoftmaxLayer)

# Monta o treinamento
trainer = BackpropTrainer(ffnet, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)

# Geração de uma grade com os pontos
ticks = arange(-3.,6.,0.2)
X, Y = meshgrid(ticks, ticks)
# Precisa de vetores de coluna no dataset, não arrays
griddata = ClassificationDataSet(2,1, nb_classes=3)
for i in range(X.size):
    griddata.addSample([X.ravel()[i],Y.ravel()[i]], [0])
griddata._convertToOneOfMany()

# Inicia o treinamento
for i in range(20):
    trainer.trainEpochs(1)
    # Avalia o treinamento e testa os dados
    trnresult = percentError(trainer.testOnClassData(), trndata['class'])
    tstresult = percentError(trainer.testOnClassData(dataset=tstdata), tstdata['class'])

    print("epoca: %4d" % trainer.totalepochs, \
          " erro de treino: %5.2f%%" % trnresult, \
          " erro de teste: %5.2f%%" % tstresult)

    # Roda a grade através da rede
    out = ffnet.activateOnDataset(griddata)
    out = out.argmax(axis=1) # O valor mais alto de saída indica a classe
    out = out.reshape(X.shape)

    # Traça os dados do teste e a grade subjacente como um contorno preenchido.
    figure(1)
    ioff()  # interactive graphics off
    clf()   # clear the plot
    hold(True) # overplot on
    for c in [0,1,2]:
        here, _ = where(tstdata['class']==c)
        plot(tstdata['input'][here,0],tstdata['input'][here,1],'o')
    if out.max()!=out.min():  # safety check against flat field
        contourf(X, Y, out)   # plot the contour
    ion()   # interactive graphics on
    draw()  # update the plot

ioff()
show()
