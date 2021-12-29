
class Matriz():
    
    def __init__(self, array):
        self.__filas = len(array)
        self.__columnas = len(array[0])
        self.__valores = array
        
    def representacion(self):
        for valor in self.__valores:
            print(valor)
    
    def getFilas(self):
        return self.__filas
    
    def getColumnas(self):
        return self.__columnas
    
    