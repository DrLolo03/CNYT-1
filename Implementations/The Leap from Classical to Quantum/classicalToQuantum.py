import matplotlib.pyplot as plot
import numpy as np

from  matrixAndVectorLibrary import *


def probabilisticSystem( matrix, vectIni, clicks ):
    if ( clicks  > 0 ) and ( type( clicks ) is int ):
        length  = len( vectIni )
        for x in range(clicks  ):
            vectIni = actionMatrixOnVector( matrix , vectIni )
            
        for el in vectIni:
            print(el[0]*100)
        return vectIni
    return -1

    
def experimentBooleanMatrix( clicks ,booleanMatrix, vectIni  ):
    if ( clicks >= 0 and type( clicks ) is int ):
        for c in range( clicks ):
            vectIni = actionBoolMatrixOnVector(booleanMatrix, vectIni)
            
        return vectIni
         

def multipleSlitExperiment( matrix , vectIni, clicks  ):
        return  probabilisticSystem( matrix , vectIni, clicks  )

def multipleSlitQuantumExperiment(  ):
        return probabilisticSystem( matrix , vectIni, clicks  )

def graphProbabilitiesVector( vector  ):
    data = len( vector )
    x = np.array([ x for x in range( data )])
    y = np.array([ round(vector[x]*100,2) for x in range( data )])

    plot.bar( x,y , color ='g', align='center')
    plot.title('Probabilidades vector')
    plot.show()
    
def main( ):
    size, clicks = int( stdin.readline().strip() ), int( stdin.readline().strip() )
    booleanMatrix = [ [ False for t in range( size )] for x in range( size  )]
    vectIni = [ False for x in range( size ) ]
##    vectIni[ 0 ] = True
##    booleanMatrix[1][0] = True  
##    booleanMatrix[1][5]=  True 
##    booleanMatrix[2][0]= True  
##    booleanMatrix[3][2]= True
##    booleanMatrix[4][3]= True
##    booleanMatrix[5][4]= True
##
##    print(clicks, experimentBooleanMatrix( clicks ,booleanMatrix, vectIni  ))
##    print()
##    print(booleanMatrix)
##    for el in experimentBooleanMatrix( clicks ,booleanMatrix, vectIni  ):
##        print( el )
    

#Author : Iván Camilo Rincón Saavedra
