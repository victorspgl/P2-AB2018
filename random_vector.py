# Modulo de generacion de grafo aleatorio en fichero txt.
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

import random
from Vector import Vector

def random_vector(conFichero, num_elementos, max):
    if num_elementos <= 0:
        print("Numero de elementos del vector debe ser superior a 0")
        raise Exception

    if conFichero:
        fichero_objeto = open("random_graph.txt", "w")
        fichero_objeto.write(str(num_elementos) + "\n")

    configuracion = Vector(num_elementos)

    for i in range(0,num_elementos):

        elemento = random.randint(1, max)

        configuracion.setElement(i,elemento)

    if conFichero:
        for i in range(0,num_elementos):

            elemento = configuracion.elements[i]
            fichero_objeto.write(str(elemento) + " ")
        fichero_objeto.write("\n")
        fichero_objeto.close()

    return configuracion

