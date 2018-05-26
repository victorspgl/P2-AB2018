# Programa Principal. Lectura de ficheros y querys
# Javier Corbalan y Victor Soria
# 16 Mayor 2018

import cProfile
from description_file_reader import read_description
from random_vector import random_vector
from random_vector import worst_random_vector

import sys

########################################################################################################################
#############################         Funciones de entrada de comandos         #########################################
########################################################################################################################

def muestra_ayuda():
    print(" El comando 'c' permite cambiar fichero de referencia")
    print(" Este fichero debe seguir el siguiente formato:")
    print("    El fichero debe contener en la primera linea el numero de elementos del vector")
    print("    en la segunda linea debe describirse cada elemento del vector como un entero separado del siguiente elemento")
    print("    Ver Ejemplo vector_basico.txt")
    print(" El comando 'o1' ordena el vector con el criterio 1, el pivote es el primer elemento del vector")
    print(" El comando 'o2' ordena el vector con el criterio 2, el pivote es la mediana")
    print(" El comando 'o3' ordena el vector con el criterio 3, el pivote es un elemento aleatorio del vector")
    print(" El comando 'r' permite crear un vector aleatorio, especificandolo de la siguiente manera:")
    print("    numero_de_elementos_del_vector, tamanyo maximo de cada elemento")
    print(" El comando 'rf' permite crear un vector aleatorio y guardarlo en un fichero")
    print(" El comando 'wr' permite crear un vector ordenado")
    print(" El comando 'wrf' permite crear un vector ordenado y guardarlo en un fichero")


""" Funcion que pide al usuario el nombre de un fichero y lo intenta interpretar. Si el fichero no es valido lo vuelve
    a intentar. """

def leer_nombre_fichero():
    correcto = False
    while not correcto:
        nombre_fichero = raw_input("Introduce fichero de entrada: ")

        try:
            configuracion = read_description(nombre_fichero)
            correcto = True
        except:
            print("Fichero en formato incorrecto o ilegible")

    return configuracion


""" Funcion que pide al usuario la descripcion del vector. Si la descripcion no es valida lo vuelve a intentar. """


def leer_descripcion(conFichero, ordenado):
    correcto = False
    while not correcto:
        string = raw_input("Introduce numero de elementos y el tamanyo maximo de cada elemento: ")

        try:
            num_elementos, max = [int(i) for i in string.split(' ')]
        except:
            print("Descripcion en formato incorrecto")
            continue

        try:
            if ordenado:
                configuracion = worst_random_vector(conFichero, num_elementos, max)
            else:
               configuracion = random_vector(conFichero, num_elementos, max)
        except:
            print("Error al crear el fichero")
            continue

        correcto = True

    return configuracion

""" Funcion que comprueba la ordenacion del vector """


def comprobar(vector):
    correcto = True
    iter = 0
    while correcto == True and iter < (len(vector) - 1):
        correcto = vector[iter] <= vector[iter + 1]
        iter = iter + 1
    return correcto

########################################################################################################################
##########################################         MAIN         ########################################################
########################################################################################################################

sys.setrecursionlimit(150000)
fichero_referencia = False

print("Introduce un comando:")
print("c - cambiar fichero de referencia")
print("o1 - ordena el vector con el criterio 1")
print("o2 - ordena el vector con el criterio 2")
print("o3 - ordena el vector con el criterio 3")
print("r - crear un vector aleatorio en memoria")
print("rf - crear un vector aleatorio en un fichero y cargarlo en memoria")
print("wr - crear un vector ordenado en memoria")
print("wrf - crear un vector ordenado en un fichero y cargarlo en memoria")
print("h - ayuda")

while True:

    comando = raw_input("$$: ")

    if (comando == "c"):
        configuracion = leer_nombre_fichero()
        fichero_referencia = True
    elif (comando == "o1"):
        if fichero_referencia == False:
            print("No existe un vector para ordenar, utiliza c para introducirlo mediante fichero o r para generar uno aleatorio")
            continue
        cProfile.run('configuracion.sort1()')
        vector = configuracion.sort1()
        correcto = comprobar(vector)
        if correcto:
            print(" -> Vector ordenado correctamente ")
        else:
            print(" -> Vector ordenado incorrectamente ")
    elif (comando == "o2"):
        if fichero_referencia == False:
            print("No existe un vector para ordenar, utiliza c para introducirlo mediante fichero o r para generar uno aleatorio")
            continue
        cProfile.run('configuracion.sort2()')
        vector = configuracion.sort2()
        correcto = comprobar(vector)
        if correcto:
            print(" -> Vector ordenado correctamente ")
        else:
            print(" -> Vector ordenado incorrectamente ")
    elif (comando == "o3"):
        if fichero_referencia == False:
            print("No existe un vector para ordenar, utiliza c para introducirlo mediante fichero o r para generar uno aleatorio")
            continue
        cProfile.run('configuracion.sort3()')
        vector = configuracion.sort3()
        correcto = comprobar(vector)
        if correcto:
            print(" -> Vector ordenado correctamente ")
        else:
            print(" -> Vector ordenado incorrectamente ")
    elif (comando == "h"):
        muestra_ayuda()
    elif (comando == "rf"):
        configuracion = leer_descripcion(True, False)
        fichero_referencia = True
    elif (comando == "r"):
        configuracion = leer_descripcion(False, False)
        fichero_referencia = True
    elif (comando == "wrf"):
        configuracion = leer_descripcion(True, True)
        fichero_referencia = True
    elif (comando == "wr"):
        configuracion = leer_descripcion(False, True)
        fichero_referencia = True
    else:
        print("Comando incorrecto")
        muestra_ayuda()

    print("Introduce un comando:")
