# Modulo de generacion de vectores aleatorios
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

import random
from Vector import Vector


"""
    Genera un vector, y en caso de que conFichero sea igual a True genera un fichero, "random_vector.txt", que contiene
    una descripcion de un vector de acuerdo al formato establecido en el fuente description_file_reader.py.
    La funcion genera elementos aleatorios del vector.
"""
def random_vector(num_vectores, conFichero, num_elementos, max):
    if num_elementos <= 0:
        print("Numero de elementos del vector debe ser superior a 0")
        raise Exception

    if conFichero:
        fichero_objeto = open("random_vector.txt", "w")
        fichero_objeto.write(str(num_vectores) + " " + str(num_elementos) + "\n")

    for j in range(0, num_vectores):

        if j == 0:
            configuracion = Vector(num_elementos)

        for i in range(0, num_elementos):

            elemento = random.randint(1, max)

            if j == 0:
                configuracion.setElement(i,elemento)

            if conFichero:
                if i == (num_elementos - 1):
                    fichero_objeto.write(str(elemento) + "\n")
                else:
                    fichero_objeto.write(str(elemento) + " ")
    if conFichero:
        fichero_objeto.close()

    return configuracion

"""
    Genera un vector ordenado, y en caso de que conFichero sea igual a True genera un fichero, "random_vector.txt",
    que contiene una descripcion de un vector de acuerdo al formato establecido en el fuente description_file_reader.py.
    La funcion genera elementos ordenados de forma a inversa, para generar pruebas en el caso peor.
"""
def worst_random_vector(conFichero, num_elementos):
    if num_elementos <= 0:
        print("Numero de elementos del vector debe ser superior a 0")
        raise Exception

    if conFichero:
        fichero_objeto = open("random_vector.txt", "w")
        fichero_objeto.write(str(1) + " " + str(num_elementos) + "\n")

    configuracion = Vector(num_elementos)

    for i in range(0, num_elementos):

        elemento = num_elementos - i

        configuracion.setElement(i,elemento)

        if conFichero:
            if i == (num_elementos - 1):
                fichero_objeto.write(str(elemento))
            else:
                fichero_objeto.write(str(elemento) + " ")

    if conFichero:
        fichero_objeto.write("\n")
        fichero_objeto.close()

    return configuracion