from sys import stdin 
from  matrixAndVectorLibrary import *

def experimentBooleanMatrix( clicks ,booleanMatrix, vectIni  ):
    if ( clicks >= 0 and type( clicks ) is int ):
        for c in range( clicks ):
            vectIni = actionBoolMatrixOnVector(booleanMatrix, vectIni)
            
        return vectIni
         

def multipleSlitExperiment(  ):
        pass

def multipleSlitQuantumExperiment(  ):
        pass

def graphProbabilitiesVector(  ):
        pass



def main( ):
    size, clicks = int( stdin.readline().strip() ), int( stdin.readline().strip() )
    booleanMatrix = [ [ False for t in range( size )] for x in range( size  )]
    vectIni = [ False for x in range( size ) ]
    vectIni[ 0 ] = True
    booleanMatrix[1][0] = True  
    booleanMatrix[1][5]=  True 
    booleanMatrix[2][0]= True  
    booleanMatrix[3][2]= True
    booleanMatrix[4][3]= True
    booleanMatrix[5][4]= True

    print(clicks, experimentBooleanMatrix( clicks ,booleanMatrix, vectIni  ))
    print()
    print(booleanMatrix)
    for el in experimentBooleanMatrix( clicks ,booleanMatrix, vectIni  ):
        print( el )

#Author : Iván Camilo Rincón Saavedra
