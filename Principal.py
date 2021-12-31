
from Matriz import Matriz
import numpy as np

def run ():
    
    
    A = np.array([[1, 2, 3],[2, 1, 4]])
    B = np.array([[1,0],[2, 1], [3, 2]])
    C = np.array([[3, -1, 3],[4, 1, 5], [2, 1, 3]])
    D = np.array([[3,-2],[2, 4]])
    E = np.array([[-1, 5],[5, 8]])
    i = np.array([[1, 0],[0, 1]])

    ma = Matriz(A)
    mb = Matriz(B)
    mc = Matriz(C)
    md = Matriz(D)
    me = Matriz(E)
    identidad = Matriz(i)
    
    a = ma.multEscalar(2).traspuesta()
    a.representacion()
    
    b = md.multMat(md)
    b.representacion()
    
    c = me.multEscalar(2)
    c.representacion()
    
    c = b.resta(c)
    c.representacion()
    
    c = c.suma(identidad.multEscalar(2))
    c.representacion()
    
    ma.multEscalar(2).suma(mb.traspuesta()).representacion()
    
    ma.multMat(mb).representacion()

    A = np.array([[2, 1, -2],[3, 2, 5]])
    B = np.array([[2,-1],[3, 4], [1, -2]])
    C = np.array([[2, 1, 3],[-1, 2, 4], [3, 1, 0]])
    D = np.array([[2,-1],[-3, 2]])

    ma = Matriz(A)
    mb = Matriz(B)
    mc = Matriz(C)
    md = Matriz(D)
    
    print("Ejercicio 2.a")
    (mb.traspuesta().suma(ma)).multMat(mc).representacion()
    
    print("Ejercicio 2.b")
    
    mb.traspuesta().representacion()
    mb.traspuesta().multMat(mc).representacion()
    (mb.traspuesta().multMat(mc)).suma(ma).representacion()
    
    A = np.array([[1, 2],[3, 2]])
    B = np.array([[2,-1],[-3, 4]])

    ma = Matriz(A)
    mb = Matriz(B)
    
    ma.multMat(mb).representacion()
    mb.multMat(ma).representacion()
    
    #Guia 2 !
    
    A = np.array([[1, -2, 1],[0, 3, 1]])
    B = np.array([[1, 2, 3],[8, -1, -1]])

    ma = Matriz(A)
    mb = Matriz(B)

    #det(A B^t)
    
    print((ma.multMat(mb.traspuesta())).determinante())
    
    #inversas
    
    A = np.matrix([[1, 3, -2],[2, 4, 0],[3, 5, -1]])
    B = np.matrix([[-3, -4], [2, 1]])

    ma = Matriz(A)
    mb = Matriz(B)
    
    ma.inversa(3)
    mb.inversa(2)
    
    #identidad
    print(ma.identidad(10))
    
    
if __name__ == '__main__':
    run()