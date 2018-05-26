
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
        for i in range(izq, dch+1):
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
        lista_aux = self.elements
        resultado = self.sort1RE(0, self.size-1)
        self.elements = lista_aux
        return resultado

    def sort1RE(self, izq, dch):
        if izq >= dch:
            return self.elements
        else:
            pivote_index = izq
            pivote_index = self.particion(izq, dch, pivote_index)
            self.sort1RE(izq, pivote_index - 1)
            self.sort1RE(pivote_index + 1, dch)
            return self.elements

    """
        QuickSort eligiendo la mediana como pivote
    """
    def sort2(self):
        lista_aux = self.elements
        resultado = self.sort2RE(0, self.size - 1)
        self.elements = lista_aux
        return resultado

    def sort2RE(self, izq, dch):
        if izq >= dch:
            return self.elements
        else:
            pivote_index = self.select(izq, dch, int((dch+izq)/2))
            pivote_index = self.particion(izq, dch, pivote_index)
            self.sort2RE(izq, pivote_index - 1)
            self.sort2RE(pivote_index + 1, dch)
            return self.elements

    def select(self, izq, dch, n):
        while True:
            if izq == dch:
                return izq

            pivotIndex = self.median(izq, dch)
            pivotIndex = self.particion(izq, dch, pivotIndex)
            if n == pivotIndex:
                return n
            elif n < pivotIndex:
                dch = pivotIndex - 1
            else:
                izq = pivotIndex + 1


    def median(self, izq, dch):
        num_elem = dch - izq
        if num_elem < 5:
            return self.insertionSort(izq, dch)
        for iter in range(izq, dch, 5):
            subDch = iter + 4
            if subDch > dch:
                subDch = dch

            median5 = self.insertionSort(iter, subDch)
            aux = self.elements[median5]
            self.elements[median5] = self.elements[izq + int((iter - izq)/5)]
            self.elements[izq + int((iter - izq)/5)] = aux

        return self.select(izq, izq + int((dch - izq) / 5), izq + int((dch - izq) / 10))

    def insertionSort(self, izq, dch):
        i = 1
        while i < (dch - izq + 1):
            j = i + izq
            while j > 0 and self.elements[j - 1] > self.elements[j]:
                aux = self.elements[j - 1]
                self.elements[j - 1] = self.elements[j]
                self.elements[j] = aux
                j = j - 1
            i = i + 1
        return int((dch + izq)/2)


    """
       QuickSort eligiendo como pivote un elemento aleatorio del vector 
    """
    def sort3(self):
        lista_aux = self.elements
        resultado = self.sort3RE(0, self.size - 1)
        self.elements = lista_aux
        return resultado

    def sort3RE(self, izq, dch):
        if izq >= dch:
            return self.elements
        else:
            pivote_index = int(random.uniform(izq, dch))
            pivote_index = self.particion(izq, dch, self.elements[pivote_index])
            self.sort3RE(izq, pivote_index - 1)
            self.sort3RE(pivote_index + 1, dch)
            return self.elements