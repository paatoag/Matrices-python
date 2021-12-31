
from Matriz import Matriz
import numpy as np

def run ():
    
    A = np.array([[-3, 4, 1],[0, 3, -2], [4, 5, 3]])
    B = np.array([[3,-1, 1],[0, -2, 4], [5, 3, 1]])
    
    ma = Matriz(A)
    mb = Matriz(B)
    
    ma.representacion()
    mb.representacion()
    
    #suma
    ma.suma(mb).representacion()
 
    #resta
    resultado = ma.resta(mb)
    resultado.representacion()
    
    #multiplicacion (k)
    resultado = ma.multEscalar(5)
    resultado.representacion()
    
    A = np.array([[4, -2, 3],[5, -1, 0]])
    B = np.array([[3, 0, 1],[-2, 4, 5], [2, 3, -4]])
    
    ma = Matriz(A)
    mb = Matriz(B)
    
    #multiplicacion
    resultado = ma.multMat(mb)
    resultado.representacion()
    
    #traspuesta
    resultado = ma.traspuesta()
    resultado.representacion()
    
    #identidad
    identidad = Matriz(np.eye(10, dtype = int))
    identidad.representacion()
    
    C = np.array([[-2, 0, 5],[4, -5, 2], [1, 4, 2]])
    mc = Matriz(C)
    
    #determinante
    determinante = mc.determinante()
    print(int(determinante))
    
    C = np.matrix([[-2, 0, 5],[4, -5, 2], [1, 4, 2]])
    mc = Matriz(C)
    
    #matriz inversa
    inversa = mc.inversa()
    print(inversa)

    print(mc.showInversa(inversa))
            
if __name__ == '__main__':
    run()