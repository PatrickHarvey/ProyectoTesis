# ProyectoTesis

Generación de melodia midi y partitura a partir de señal de audio monofónica

YouTube: https://youtu.be/0TXa5fJMxsQ

Universidad Nacional San Agustín

Ciencia de la Computación

- Alumno: Norman Patrick Harvey Arce


Objetivo General:
* El objetivo del siguiente proyecto de tesis es automatizar el proceso de crear una melodía, con su respectiva partitura, a partir de un archivo de entrada que contenga una señal de audio monofónica, es decir notas musicales.

Objetivos Específicos:
* Identificar las notas presentes en el archivo de entrada
* Crear un archivo \textit{midi} con la secuencia de notas identificadas
* Generar una partitura en base al archivo 

Herramientas adicionales:
- JythonMusic (Editor Midi)
- Colin'sHume (Conversión partituras)

Librerías utilizadas:
- PyAudio
- Aubio

A continuación, se listan las funciones del algoritmo utilizado para este proyecto:
- Archivo de entrada
- Paso a la transformación de dominio
- Transformada Rápida de Fourier
- Tratamiento de la señal
- Coeficientes Cepstrales en las Frecuencias de Mel
- Secuencia de Notas 
- Conversión a formato midi
- Paso al editor de midi
- JythonMusic
- Generando Archivo midi
- Primer Archivo de Salida
- Conversión a formato pdf
- Paso al editor de partituras
- ABC2MIDI
- Generando Archivo pdf
- Segundo Archivo de Salida

Imágenes:
* diagrama_de_flujo.png: Se enumeran los procesos mencionados anteriormente
* diagrama_b loques_2.png: Se grafica los procesos que realiza el algoritmo
