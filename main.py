import os
import sys

filename = sys.argv[1]
os.system("aubio notes " + filename)
os.system("python plot.py")
os.system("python transcribir.py")
os.system("python partitura.py")
