# Lector de ficheros de descripcion del grafo
# Javier Corbalan y Victor Soria
# 15 Marzo 2018

from Vector import Vector

#
# Lee un fichero de descripcion que contiene en la primera fila el numero de elementos del vector y a continuacion el
#   fichero describe en la segunda linea cada elemento separado por un espacio.
#

def read_description(nombre_fichero):
    fichero_objeto = open(nombre_fichero, "r")
    lineas = fichero_objeto.readlines()
    num_elem = [int(i) for i in lineas[0].split(' ')]

    configuracion = Vector(num_elem[0])

    elementos = [int(i) for i in lineas[1].split(' ')]

    for iter in range(0, num_elem[0]):
        configuracion.setElement(iter,elementos[iter])

    return configuracion
