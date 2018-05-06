

class Vector:

    def __init__(self, size):
        self.size = size
        self.elements = []
        for i in range(0,size):
            self.elements.append(0)

    def setElement(self, index, element):
        self.elements[index] = element

    def sort1(self):
        self.sort1RE(0,self.size)

    def sort1RE(self, izq, dch):
        if izq > dch:
            return
        else:
            pivote = self.elements[izq]
            pivote_index = 0
            #ordenar
            self.sort1RE(izq, pivote_index)
            self.sort1RE(pivote_index, dch)
            return

    def sort2(self):
        self.sor2RE(0,self.size)

    def sort2RE(self, izq, dch):
        if izq > dch:
            return