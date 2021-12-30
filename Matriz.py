
import numpy as np

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
        print("-"*5 + "suma" + "-"*5 + "\n")
        return Matriz(self.getValores() + np.mat(b.getValores()))
    
    def resta(self, b):
        print("-"*5 + "resta" + "-"*5 + "\n")
        return Matriz(self.getValores() - np.mat(b.getValores()))
    
    def multEscalar(self, k):
        print("-"*5 + "multiplicacion (k)" + "-"*5 + "\n")       
        return Matriz(np.mat(self.getValores() * k))
    
    def multMat(self, b):
        print("-"*5 + "multiplicación" + "-"*5 + "\n")
        return Matriz(np.matmul(self.getValores(), b.getValores()))
    
    def traspuesta(self):
        print("-"*5 + "traspuesta" + "-"*5 + "\n")
        return Matriz(self.getValores().T)
    
    def determinante(self):
        print("-"*5 + "determinante" + "-"*5 + "\n")
        return np.linalg.det(self.getValores())

    def inversa(self):
        aux = Matriz()

        return 0
    
    def getFilas(self):
        return self.__filas
    
    def getColumnas(self):
        return self.__columnas
    
    def getValores(self):
        return self.__valores
    