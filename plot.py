from csv import reader
import numpy as np
import math
import codecs
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for fila in csv_reader:
			if not fila:
				continue
			dataset.append(fila)
	return dataset	

def string_a_float(dataset, columna):
	for fila in dataset:
		fila[columna] = float(fila[columna].strip())

filename = 'plot.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
	string_a_float(dataset, i)

x = []
y = []
for i in range(len(dataset)):
    x.append(dataset[i][0])
    y.append(dataset[i][1])

fig = plt.figure()
#plt.title('')
plt.xlabel('Tiempo')
plt.ylabel('Frecuencia - MIDI')
plt.plot(y, x, marker='o')
plt.savefig("cuadro.png")
plt.show()

