
from Matriz import Matriz
import numpy as np

def run ():
    array_bi = [[1, 2],
                [3, 4]]
    
    ma = Matriz(array_bi)
    
    ma.representacion()
    
if __name__ == '__main__':
    run()