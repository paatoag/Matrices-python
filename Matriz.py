
import numpy as np
from numpy.core import numeric

class Matriz():
    
    def __init__(self, array):
        self.__filas = len(array)
        self.__columnas = len(array[0])
        self.__valores = array
        
    def representacion(self):
        for valor in self.__valores:
            print(valor)
        print("\n")
    
    def suma(self, b):
        return Matriz(self.getValores() + np.mat(b.getValores()))
    
    def resta(self, b):
        return Matriz(self.getValores() - np.mat(b.getValores()))
    
    def multEscalar(self, k):     
        return Matriz(np.mat(self.getValores() * k))
    
    def multMat(self, b):
        return Matriz(np.matmul(self.getValores(), b.getValores()))
    
    def traspuesta(self):
        return Matriz(self.getValores().T)
    
    def determinante(self):
        return np.linalg.det(self.getValores())

    def showInversa(self, inversa, tamano):
        det = int(self.determinante())
        texto = ""
        
        if tamano == 3:
            for i in range(self.__filas):
                num1 = int(inversa[i, 0] * det)
                num2 = int(inversa[i, 1] * det)
                num3 = int(inversa[i, 2] * det)
                texto += f"{num1}/{det} | {num2}/{det} | {num3}/{det} |\n"
        elif tamano == 2:
            for i in range(self.__filas):
                num1 = int(inversa[i, 0] * det)
                num2 = int(inversa[i, 1] * det)
                texto += f"{num1}/{det} | {num2}/{det} |\n"
        print(texto)
        
    def inversa(self, tamano):
        inversa = self.getValores().I
        return self.showInversa(inversa, tamano)
    
    def identidad(self, tamano):
        return np.eye(tamano, dtype = int)
    
    def getFilas(self):
        return self.__filas
    
    def getColumnas(self):
        return self.__columnas
    
    def getValores(self):
        return self.__valores