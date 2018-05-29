# Lector de ficheros de descripcion de vectores
# Javier Corbalan y Victor Soria
# 15 Mayo 2018

from Vector import Vector

#
# Lee un fichero de descripcion que contiene en la primera fila el numero de vectores almacenados y el
#   numero de elementos por vector y a continuacion se describe en cada linea un vector
#   El vector esta compuesto por elementos separados por un espacio.
#   LA FUNCION DEVUELVE UNA LISTA CON TODOS LOS VECTORES.
#
def read_description(nombre_fichero):
    fichero_objeto = open(nombre_fichero, "r")
    lineas = fichero_objeto.readlines()
    num_vectores, num_elem = [int(i) for i in lineas[0].split(' ')]

    lista_configuraciones = []
    for iter in range(1, num_vectores+1):
        configuracion = Vector(num_elem)

        elementos = [int(i) for i in lineas[iter].split(' ')]

        configuracion.setAllElements(elementos)

        lista_configuraciones.append(configuracion)

    fichero_objeto.close()
    return lista_configuraciones

#
# Lee un fichero de descripcion que contiene en la primera fila el numero vectores en el fichero
#   y el numero de elementos por vector y a continuacion el fichero describe en la cada linea un vector.
#   El vector esta compuesto por elementos separados por un espacio.
#   DEL FICHERO SOLO ALMACENA EN MEMORIA EL PRIMER VECTOR
#
def read_description_one(nombre_fichero):
    fichero_objeto = open(nombre_fichero, "r")
    lineas = fichero_objeto.readlines()
    num_vectores, num_elem = [int(i) for i in lineas[0].split(' ')]

    configuracion = Vector(num_elem)

    elementos = [int(i) for i in lineas[1].split(' ')]

    configuracion.setAllElements(elementos)

    return configuracion
