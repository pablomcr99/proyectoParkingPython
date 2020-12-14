from io import open
from datetime import datetime,timedelta

"""fichero = open('ficheros/prueba.txt','w')

texto="alo prresidentess"
fichero.write(texto)

fichero = open('ficheros/prueba.txt','a')

texto2=", alo prresidentess2"
fichero.write(texto2)

fichero = open('ficheros/prueba.txt','r')

texto = fichero.readlines()

fichero.close()
print(texto)"""
fechaActiv=datetime.now()
fechaFinal=fechaActiv+timedelta(days=30)
print(fechaFinal)


