
import re
ruta = input("Escribir el archivo de registro a procesar: ")
expresion_regular = input("Escribir la expresión regular: ")

#Ejemplo de entradas:
#ruta = C:\Users\arcad\Downloads\AdobeARM.log
#expresion_regular = '\*\* Setting Error Condition'

with open(ruta,'r') as archivo:
    for linea in archivo:
        if re.search(expresion_regular, linea):
            print(linea)


