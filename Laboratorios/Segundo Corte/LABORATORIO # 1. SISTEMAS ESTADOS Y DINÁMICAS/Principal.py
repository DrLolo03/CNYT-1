from sys import stdin
from matrixAndVectorLibrary import *

def deterministicSystem( matrix , vectIni, clicks  ):
    if ( clicks  > 0 ) and ( type( clicks ) is int ):
        length  = len( vectIni )
        for x in range(1, clicks   ):
            vectIni = actionMatrixOnVector( matrix , vectIni )

        vectAnsw = actionMatrixOnVector(  matrix , vectIni )
        for el in vectAnsw:
            print(el)
        return vectAnsw
    return vectIni

def probabilisticSystem( matrix, vectIni, clicks ):
    if ( clicks  > 0 ) and ( type( clicks ) is int ):
        length  = len( vectIni )
        for x in range(1, clicks   ):
            vectIni = actionMatrixOnVector( matrix , vectIni )
        vectAnsw = actionMatrixOnVector(  matrix , vectIni )
        for el in vectAnsw:
            print(el[0]*100)
        return vectAnsw
    return vectIni
    
    


def deterministaEjercicio(  ):
    """PRE: no recibe ningun argumento
     POST: calcula el resultado deseado de el  LABORATORIO # 1. SISTEMAS: ESTADOS Y DINÁMICAS """
    matrix = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]], [[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0]], [[0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]], [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
    vector = [[0,0] for c in range( len( matrix ) ) ]
    
    print( "que ejercicio del taller es ?")
    case = int( stdin.readline().strip() )

    print("numero de clicks")
    clicks = int( stdin.readline().strip() )

    if case == 1:
        vector = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]] 
            
    elif  case == 2:
        vector = [[6, 0], [0, 0], [3, 0], [5, 0], [3, 0], [8, 0]] 

    elif case == 3:
        vector = [[6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0]]
    else :
        #ejemplo del libro, ejercicio en clase
        matrix = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [1, 0], [1, 0], [0, 0]], [[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0]], [[0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]], [[1, 0], [0, 0], [1, 0], [0, 0], [1, 0], [0, 0]], [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]] 
        vector = [[3, 0], [2, 0], [3, 0], [0, 0], [5, 0], [7, 0]]

    deterministicSystem( matrix , vector, clicks )
    

def probabilisticoEjercicio ():
    """PRE: no recibe ningun argumento
    POST: calcula el resultado deseado de el  LABORATORIO # 1. SISTEMAS: ESTADOS Y DINÁMICAS """
    
    print("ingrese el tamaño de la matriz m")
    size = int( stdin.readline().strip() )

    print("ingrese el tamaño de la matriz n")
    size2 = int( stdin.readline().strip() )

    print("numero de clicks")
    cliks = int( stdin.readline().strip() )
    
    M = [[[0, 0], [0.16666666666666666, 0], [0.8333333333333334, 0]], [[0.3333333333333333, 0], [0.5, 0], [0.16666666666666666, 0]], [[0.6666666666666666, 0], [0.3333333333333333, 0], [0, 0]]]
    N = [[[0.3333333333333333, 0], [0.6666666666666666, 0]], [[0.6666666666666666, 0], [0.3333333333333333, 0]]]
    
    vector = [[0.8, 0], [0.2, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    newMatrix  = tensorProduct( M,N )
    answ = probabilisticSystem( newMatrix, vector, cliks )
          
    
def main():
    deterministaEjercicio(  )
    print("-----")
    probabilisticoEjercicio(  )

#Author : Iván Camilo Rincón Saavedra
