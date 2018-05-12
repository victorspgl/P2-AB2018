
import random

class Vector:

    def __init__(self, size):
        self.size = size
        self.elements = []
        for i in range(0,size):
            self.elements.append(0)

    def setElement(self, index, element):
        self.elements[index] = element


    """
        Divide un vector en dos zonas, una con todos los elementos del vector
        menores que el pivote y otra con todos los elementos mayores que el
        pivote.
    """
    def particion(self, izq, dch, pivoteIndex):
        pivote = self.elements[pivoteIndex]
        self.elements[pivoteIndex] = self.elements[dch]
        self.elements[dch] = pivote
        storeIndex =  izq
        for i in range(izq, dch):
            if self.elements[i] < pivote:
                aux = self.elements[storeIndex]
                self.elements[storeIndex] = self.elements[i]
                self.elements[i] = aux
                storeIndex = storeIndex + 1
        self.elements[dch] = self.elements[storeIndex]
        self.elements[storeIndex] = pivote
        return storeIndex


    """
        QuickSort eligiendo como pivote el elemento mas a la izquierda del vector.
    """
    def sort1(self):
        self.sort1RE(0, self.size)

    def sort1RE(self, izq, dch):
        if izq > dch:
            return
        else:
            pivote_index = izq
            pivote_index = self.particion(izq, dch, pivote_index)
            self.sort1RE(izq, pivote_index)
            self.sort1RE(pivote_index, dch)
            return

    """
        QuickSort eligiendo la mediana como pivote
    """
    def sort2(self):
        self.sort2RE(0, self.size)

    def sort2RE(self, izq, dch):
        if izq > dch:
            return
        else:
            pivote_index = self.median(self.elements, izq, dch)
            pivote_index = self.particion(izq, dch, pivote_index)
            self.sort2RE(izq, pivote_index)
            self.sort2RE(pivote_index, dch)
            return

    def median(self, lista, izq, dch):
        num_elem = dch - izq
        if num_elem < 5:
            return self.insertionSort(lista, izq, dch)
        lista = []
        new_num_elem = 0
        for iter in range(0, num_elem, 5):
            subDch = iter + 4
            if subDch > num_elem:
                subDch = num_elem

            median5 = self.insertionSort(lista, iter, subDch)
            lista.append(median5)
            new_num_elem = new_num_elem + 1
        self.median(lista, 0, new_num_elem)

    def insertionSort(self, lista, izq, dch):


    """
       QuickSort eligiendo como pivote un elemento aleatorio del vector 
    """
    def sort3(self):
        self.sort3RE(0, self.size)

    def sort3RE(self, izq, dch):
        if izq > dch:
            return
        else:
            pivote_index = random.uniform(izq, dch)
            self.particion(izq, dch, pivote_index)
            self.sort3RE(izq, pivote_index)
            self.sort3RE(pivote_index, dch)
            return