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


def convertir(valor_int):
    if valor_int == 48:
        return "C"
    elif valor_int == 49:
        return "^C"
    elif valor_int == 50:
        return "D"
    elif valor_int == 51:
        return "^D"
    elif valor_int == 52:
        return "E"
    elif valor_int == 53:
        return "F"
    elif valor_int == 54:
        return "^F"
    elif valor_int == 55:
        return "G"
    elif valor_int == 56:
        return "^G"
    elif valor_int == 57:
        return "A"
    elif valor_int == 58:
        return "^A"
    elif valor_int == 59:
        return "B"
    elif valor_int == 60:
        return "c"
    elif valor_int == 61:
        return "^c"
    elif valor_int == 62:
        return "d"
    elif valor_int == 63:
        return "^d"
    elif valor_int == 64:
        return "e"
    elif valor_int == 65:
        return "f"
    elif valor_int == 66:
        return "^f"
    elif valor_int == 67:
        return "g"
    elif valor_int == 68:
        return "^g"
    elif valor_int == 69:
        return "a"
    elif valor_int == 70:
        return "^a"
    elif valor_int == 71:
        return "b"
    elif valor_int == 72:
        return "c'"
    elif valor_int == 73:
        return "^c'"
    elif valor_int == 74:
        return "d'"
    elif valor_int == 75:
        return "^d'"
    elif valor_int == 76:
        return "e'"
    elif valor_int == 77:
        return "f'"
    elif valor_int == 78:
        return "^f'"
    elif valor_int == 79:
        return "g'"
    elif valor_int == 80:
        return "^g'"
    elif valor_int == 81:
        return "a'"
    elif valor_int == 82:
        return "^a'"
    elif valor_int == 83:
        return "b'"
    elif valor_int == 84:
        return "c''"
    elif valor_int == 85:
        return "^c''"
    else:
        return "z"


f = open("/home/patrick/TESIS/partitura.txt", "w")

f.write("X:1\n")
f.write("T:Composicion\n")
f.write("M:C\n")
f.write("L:1/4\n")
f.write("K:C\n")

j = 0

for i in range(len(dataset)):
    f.write(convertir(dataset[i][0])+" ")  #    f.write(str(dataset[i][0])+" ")
    j+=1
    if j == 4:
        f.write("| ")
        j=0
f.write("]\n")

#C, D, E, F,|G, A, B, C|D E F G|A B c d|e f g a|b c' d' e'|f' g' a' b'|]







