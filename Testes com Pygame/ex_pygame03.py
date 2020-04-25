from pygame_functions import *
import random

screenSize(800,800)

instructionLabel = makeLabel('Please enter a word', 40, 10, 700, 'blue', 'Agency FB', 'yellow')
showLabel(instructionLabel)

wordBox = makeTextBox(10, 750, 300, 0, 'Digite seu texto aqui', 15, 24)
showTextBox(wordBox)
entrada = textBoxInput(wordBox)
print(entrada)

box1 = makeLabel('X', 32, 50, 50, 'blue', 'Arial', 'white')
showLabel(box1)


endWait()
