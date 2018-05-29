# Programa Principal. Lectura de ficheros y comandos
# Javier Corbalan y Victor Soria
# 16 Mayor 2018

from description_file_reader import read_description
from description_file_reader import read_description_one
from random_vector import random_vector
from random_vector import worst_random_vector
import time

import sys

########################################################################################################################
#############################         Funciones de entrada de comandos         #########################################
########################################################################################################################

"""
    Muestra una guia con los comandos disponibles
"""
def muestra_ayuda():
    print(" El comando 'c' permite cambiar fichero de referencia")
    print(" Este fichero debe seguir el siguiente formato:")
    print("    El fichero debe contener en la primera linea el numero vectores y el numero de elementos por vector")
    print("    El fichero debe describir en cada linea un vector. La descripcion consiste en cada elemento del vector")
    print("    representado como un entero separado del siguiente elemento")
    print("    Ver Ejemplo vector_basico.txt")
    print(" El comando 'o1' ordena el vector con el criterio 1, el pivote es el primer elemento del vector")
    print(" El comando 'o2' ordena el vector con el criterio 2, el pivote es la mediana")
    print(" El comando 'o3' ordena el vector con el criterio 3, el pivote es un elemento aleatorio del vector")
    print(" El comando 'r' permite crear un vector aleatorio, especificandolo de la siguiente manera:")
    print("    numero de elementos de cada vector, tamanyo maximo de cada elemento")
    print(" El comando 'rf' permite crear uno o mas vectores aleatorios y guardarlos en un fichero")
    print(" El comando 'wr' permite crear un vector ordenado")
    print(" El comando 'wrf' permite crear un vector ordenado y guardarlo en un fichero")


"""
    Funcion que pide al usuario el nombre de un fichero y lo intenta interpretar. Si el fichero no es valido lo vuelve
    a intentar. Si el fichero tiene mas de un vector solo recupera la informacion del primer vector
"""
def leer_nombre_fichero_one():
    correcto = False
    while not correcto:
        nombre_fichero = raw_input("Introduce fichero de entrada: ")

        try:
            configuracion = read_description_one(nombre_fichero)
            correcto = True
        except:
            print("Fichero en formato incorrecto o ilegible")

    return configuracion

"""
    Funcion que pide al usuario el nombre de un fichero y lo intenta interpretar. Si el fichero no es valido lo vuelve
    a intentar. Devuelve una lista de vectores
"""
def leer_nombre_fichero():
    correcto = False
    while not correcto:
        nombre_fichero = raw_input("Introduce fichero de entrada: ")

        try:
            configuraciones = read_description(nombre_fichero)
            correcto = True
        except:
            print("Fichero en formato incorrecto o ilegible")

    return configuraciones

"""
    Funcion que pide al usuario la descripcion para generar un vector. Si la descripcion no es valida, lo vuelve a intentar. 
"""
def leer_descripcion(conFichero, ordenado, varios_vectores):
    correcto = False
    while not correcto:
        if varios_vectores:
            string = raw_input("Introduce numero de vectores, numero de elementos y el tamanyo maximo de cada elemento: ")
        else:
            string = raw_input("Introduce numero de elementos y el tamanyo maximo de cada elemento: ")
            num_vectores = 1

        try:
            if varios_vectores:
                num_vectores, num_elementos, max = [int(i) for i in string.split(' ')]
            else:
                num_elementos, max = [int(i) for i in string.split(' ')]
        except:
            print("Descripcion en formato incorrecto")
            continue

        try:
            if ordenado:
                configuracion = worst_random_vector(conFichero, num_elementos)
            else:
                configuracion = random_vector(num_vectores, conFichero, num_elementos, max)
        except:
            print("Error al crear el fichero")
            continue

        correcto = True

    return configuracion

"""
    Funcion que comprueba la ordenacion del vector 
"""
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

sys.setrecursionlimit(1000000)
fichero_referencia = False

print("Introduce un comando:")
print("c - cambiar fichero de referencia, carga el primer vector del fichero")
print("o1 - ordena el vector con el criterio 1")
print("o2 - ordena el vector con el criterio 2")
print("o3 - ordena el vector con el criterio 3")
print("r - crear un vector aleatorio en memoria")
print("rf - crear uno o mas vectores aleatorios en un fichero y cargar el primero en memoria")
print("wr - crear un vector ordenado en memoria")
print("wrf - crear un vector ordenado en un fichero y cargalo en memoria")
print("t - para introducir un fichero con n vectores de prueba y medir los tiempos")
print("h - ayuda")

while True:

    comando = raw_input("$$: ")

    if (comando == "c"):
        configuracion = leer_nombre_fichero_one()
        fichero_referencia = True
    elif (comando == "o1"):
        if fichero_referencia == False:
            print("No existe un vector para ordenar, utiliza c para introducirlo mediante fichero o r para generar uno aleatorio")
            continue
        start = time.time()
        vector = configuracion.sort1()
        end = time.time()
        print("Tiempo de ejecucion " + str(end - start) + " segundos")
        correcto = comprobar(vector)
        if correcto:
            print(" -> Vector ordenado correctamente ")
        else:
            print(" -> Vector ordenado incorrectamente ")
    elif (comando == "o2"):
        if fichero_referencia == False:
            print("No existe un vector para ordenar, utiliza c para introducirlo mediante fichero o r para generar uno aleatorio")
            continue
        start = time.time()
        vector = configuracion.sort2()
        end = time.time()
        print("Tiempo de ejecucion " + str(end - start) + " segundos")
        correcto = comprobar(vector)
        if correcto:
            print(" -> Vector ordenado correctamente ")
        else:
            print(" -> Vector ordenado incorrectamente ")
    elif (comando == "o3"):
        if fichero_referencia == False:
            print("No existe un vector para ordenar, utiliza c para introducirlo mediante fichero o r para generar uno aleatorio")
            continue
        start = time.time()
        vector = configuracion.sort3()
        end = time.time()
        print("Tiempo de ejecucion " + str(end - start) + " segundos")
        correcto = comprobar(vector)
        if correcto:
            print(" -> Vector ordenado correctamente ")
        else:
            print(" -> Vector ordenado incorrectamente ")
    elif (comando == "h"):
        muestra_ayuda()
    elif (comando == "rf"):
        configuracion = leer_descripcion(True, False, True)
        fichero_referencia = True
    elif (comando == "r"):
        configuracion = leer_descripcion(False, False, False)
        fichero_referencia = True
    elif (comando == "wrf"):
        configuracion = leer_descripcion(True, True, False)
        fichero_referencia = True
    elif (comando == "wr"):
        configuracion = leer_descripcion(False, True, False)
        fichero_referencia = True
    elif (comando == "t"):
        lista_configuraciones = leer_nombre_fichero()
        tiempos_alg1 = []
        sum1 = 0
        tiempos_alg2 = []
        sum2 = 0
        tiempos_alg3 = []
        sum3 = 0
        for conf in lista_configuraciones:
            start = time.time()
            vector = conf.sort1()
            end = time.time()
            tiempos_alg1.append(end-start)
            sum1 = sum1 + (end-start)

            start = time.time()
            vector = conf.sort2()
            end = time.time()
            tiempos_alg2.append(end-start)
            sum2 = sum2 + (end-start)


            start = time.time()
            vector = conf.sort3()
            end = time.time()
            tiempos_alg3.append(end-start)
            sum3 = sum3 + (end-start)

        cadena = "Tiempos por vector "
        cadena1 = "Metodo 1:          "
        cadena2 = "Metodo 2:          "
        cadena3 = "Metodo 3:          "
        for i in range(0, len(lista_configuraciones)):
            cadena = cadena + "  v" + str(format(i + 1, '2.0f')) + "   "
            cadena1 = cadena1 + str(format(tiempos_alg1[i], '2.3f')) + "   "
            cadena2 = cadena2 + str(format(tiempos_alg2[i], '2.3f')) + "   "
            cadena3 = cadena3 + str(format(tiempos_alg3[i], '2.3f')) + "   "

        print(cadena)
        print(cadena1)
        print(cadena2)
        print(cadena3)


        print("Media Metodo 1: " + str(format(sum1 / len(lista_configuraciones), '2.4f')))
        print("Media Metodo 2: " + str(format(sum2 / len(lista_configuraciones), '2.4f')))
        print("Media Metodo 3: " + str(format(sum3 / len(lista_configuraciones), '2.4f')))

    else:
        print("Comando incorrecto")
        muestra_ayuda()

    print("Introduce un comando:")
