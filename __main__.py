# Programa Principal. Lectura de ficheros y querys
# Javier Corbalan y Victor Soria
# 16 Marzo 2018

import cProfile
from description_file_reader import read_description


########################################################################################################################
#############################         Funciones de entrada de comandos         #########################################
########################################################################################################################

def muestra_ayuda():
    print(" El comando 'c' permite cambiar fichero de referencia")
    print(" Este fichero debe seguir el siguiente formato:")
    # TODO: Especificar formato de los ficheros de entradaa
    print(" El comando 'o1' ordena el vector con el criterio 1")
    print(" El comando 'o2' ordena el vector con el criterio 2")
    print(" El comando 'o3' ordena el vector con el criterio 3")
    print(" El comando 'r' permite crear un vector aleatorio, especificandolo de la siguiente manera:")
    #TODO: Especificcar formato
    print(" El comando 'rf' permite crear un vector aleatorio y guardarlo en un fichero")


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


def leer_descripcion(conFichero):
    correcto = False
    while not correcto:
        string = raw_input("Introduce numero de vertices, aristas y el tiempo de comunicacion maximo: ")

        try:
            num_vertices, num_aristas, max_timestamp = [int(i) for i in string.split(' ')]
        except:
            print("Descripcion en formato incorrecto")
            continue

        try:
            configuracion = random_graph(conFichero, num_vertices, num_aristas, max_timestamp)
        except:
            print("Error al crear el fichero")
            continue

        correcto = True

    return configuracion


########################################################################################################################
##########################################         MAIN         ########################################################
########################################################################################################################

configuracion = leer_nombre_fichero()

print("Introduce un comando:")
print("c - cambiar fichero de referencia")
print("o1 - ordena el vector con el criterio 1")
print("o2 - ordena el vector con el criterio 2")
print("o3 - ordena el vector con el criterio 3")
print("r - crear un vector aleatorio en memoria")
print("rf - crear un vector aleatorio y cargarlo en memoria")
print("h - ayuda")

while True:

    comando = raw_input("$$: ")

    if (comando == "c"):
        configuracion = leer_nombre_fichero()
    elif (comando == "o1"):
        cProfile.run('configuracion.sort1()')
        vector = configuracion.sort1()
        #Comprobar ordenado
    elif (comando == "o2"):
        cProfile.run('configuracion.sort2()')
        vector = configuracion.sorter2()
        #Comprobar ordenado
    elif (comando == "o3"):
        cProfile.run('configuracion.sort3()')
        vector = configuracion.sort3()
        #Comprobar ordenado
    elif (comando == "h"):
        muestra_ayuda()
    elif (comando == "rf"):
        configuracion = leer_descripcion(True)
    elif (comando == "r"):
        configuracion = leer_descripcion(False)
    else:
        print("Comando incorrecto")
        muestra_ayuda()

    print("Introduce un comando:")
