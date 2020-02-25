import matplotlib.pyplot as plot
import numpy as np

from  matrixAndVectorLibrary import *


def probabilisticSystem( matrix, vectIni, clicks ):
    if ( clicks  > 0 ) and ( type( clicks ) is int ):
        length  = len( vectIni )
        for x in range(clicks  ):
            vectIni = actionMatrixOnVector( matrix , vectIni )
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
    y = np.array([ round(vector[x][0]*100,2) for x in range( data )])

    plot.bar( x,y , color ='g', align='center')
    plot.title('Probabilidades vector')
    plot.show()
    


#Author : Iván Camilo Rincón Saavedra
