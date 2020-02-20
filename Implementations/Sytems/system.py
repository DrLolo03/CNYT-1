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
    return -1

def probabilisticSystem( matrix, vectIni, cliks ):
    pass
    
    


def taller1( size ):
    
    matrix = [ [[0,0] for y in range ( size )] for c in range( size ) ]
    vector = [[0,0] for t in range( size )]
    
    print( "que ejercicio del taller es ?")
    case = int( stdin.readline().strip() )

    print("numero de clicks")
    cliks = int( stdin.readline().strip() )


    matrix[5][0] = [1,0]
    matrix[2][5] = [1,0]
    matrix[3][2] = [1,0]
    matrix[1][3] = [1,0]
    matrix[2][1] = [1,0]
    matrix[4][4] = [1,0]
        
    if case == 1:
        vector[5] = [1,0]
            
    elif  case == 2:
        vector[0] = [6,0]
        vector[1] = [0,0]
        vector[2] = [3,0]
        vector[3] = [5,0]
        vector[4] = [3,0]
        vector[5] = [8,0]

    elif case == 3:
        vector[0] = [6,0]
        vector[1] = [5,0]
        vector[2] = [4,0]
        vector[3] = [3,0]
        vector[4] = [2,0]
        vector[5] = [1,0]

    else :
        #ejemplo del libro, ejercicio en clase
        matrix[4][0] = [1,0]
        matrix[4][2] = [1,0]
        matrix[1][4] = [1,0]
        matrix[2][1] = [1,0]
        matrix[5][5] = [1,0]

        vector[0] = [3,0]
        vector[1] = [2,0]
        vector[2] = [3,0]
        vector[3] = [0,0]
        vector[4] = [5,0]
        vector[5] = [7,0]

    deterministicSystem( matrix , vector, clicks )
    

def taller2 ():
    print("ingrese el tamaño de la matriz m")
    size = int( stdin.readline().strip() )
    print("ingrese el tamaño de la matriz n")
    
    size2 = int( stdin.readline().strip() )
    M = [ [[0,0] for y in range ( size )] for c in range( size ) ]
    N = [ [[0,0] for y in range ( size2 )] for c in range( size2 ) ]
    
    vector = [[0,0] for t in range( size * size2 )]

    M[1][0] =[ 1/3,0]
    M[1][1] =[1/2,0]
    M[0][1] =[1/6,0]
    M[0][2] =[5/6,0]
    M[2][0] =[2/3,0]
    M[2][1] =[1/3,0]
    M[1][2] =[1/6,0]

    N[0][0]=[ 1/3,0]
    N[1][1]=[ 1/3,0]
    N[0][1]=[ 2/3,0]
    N[1][0]=[ 2/3,0]

    for el in M:
        print(el)
    print()

    for el in N:
        print(el)

    answ = tensorProduct( M,N )

    for el in answ:
        print(el)
        
          
    
def main():
    #print("ingrese el tamaño de la matriz")
    #size = int( stdin.readline().strip() )

    #taller1( size )
    #print("-----")
    taller2(  )
   
main()


    
    
    
        
#Author : Iván Camilo Rincón Saavedra
