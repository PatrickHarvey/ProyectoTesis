from csv import reader
import numpy as np
import math
import codecs

def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

def str_column_to_int(dataset, column):
	for row in dataset:
		row[column] = int(row[column].strip())

filename = 'notas.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
	str_column_to_int(dataset, i)

num_filas = len(dataset)
num_columnas = len(dataset[0])

f = open("/home/patrick/TESIS/salida.py", "w")

f.write("from music import *\n\n")

f.write("notas = [")
for i in range(len(dataset)):
    f.write(str(dataset[i][0])+", ")
f.write("]\n")

f.write("tiempos = [")
for i in range(len(dataset)):
    f.write("EN"+", ")
f.write("]\n")


f.write("tema = Phrase()\n")
f.write("tema.addNoteList(notas, tiempos)\n\n")
f.write("tema.setInstrument(25)\n\n")
f.write("Play.midi(tema)\n")
f.close()



 
#notas   = [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]

#tiempos = [QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN]










