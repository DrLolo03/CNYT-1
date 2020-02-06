import math 
from complexNumberLibrary import *

def sumVect( vect1, vect2 ):
    length = len( vect1 )
    
    if ( length == len( vect2 ) ):
            
        for x in range( length ):
                vect1[ x ] = suma( vect1[ x ], vect2[ x ] )
            
    return vect1
            

def inverseVect( vect ):
    length = len( vect )
    for x in range( length ):
        current = vect[ x ]
        vect[ x ] = conjugated( current )
        vect[ x ][ 0 ] = - current[ 0 ] 
        
    return vect


def escalVect( vect, complexNumber ):
    length = len( vect )
    
    for x in range( length ):
        vect[ x ] = multComplexNumber( complexNumber , vect[ x ] )
        
    return vect

def sumMat( mat1, mat2 ):
        row, colum  = len( mat1 ), len( mat1[ 0 ] )
         
        for i in range( row ):
                for j in range( colum ):
                        mat1[ i ][ j ] = suma ( mat1[ i ][ j ] , mat2[ i ][ j ] )
                        
        return mat1

def inverseMat( mat ):
    row, colum = len( mat ), len( mat[ 0 ] )
    
    for i in range( row ):
        mat[ i ] = inverseVect( mat[ i ] )

    return mat


def multiEscalMat( complexNumber , mat ):
    row, column = len( mat ), len( mat[ 0 ] )

    for i in range( row ):
        for j in range( column ):
            mat[ i ][ j ] = multComplexNumber( complexNumber , mat[ i ][ j ] )

    return mat

def multiplicaMat( mat1, mat2 ):

    row1, col1 = len( mat1 ),len( mat1[ 0 ] )
    row2, col2 =  len( mat2 ), len( mat2[ 0 ] )
     
    if ( col1 == row2 ):
        
        answ = [ [  [ 0,0 ]  for t in range( col2 ) ] for x in range( row1 ) ]
        
        for i in range( row1 ):
            for j in range( col2 ):
                
                current = [ 0, 0 ]
                
                for k in range( row2 ):

                    mult =  multComplexNumber( mat1[ i ][ k ], mat2[ k ][ j ]  ) 
                    
                    current =  suma( current , mult ) 
                    
                answ[ i ][ j ]  = current

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")
    

def transpMatrix( matrix ):
    row, col = len( matrix ), len( matrix[ 0 ] )
    answ  = [ [ 0 for x in range ( row ) ] for t in range( col ) ]
    
    for i in range( col ):
        for j in range( row ):
                answ[ i ][ j ] = matrix[ j ][ i ]
                
    return answ


def conjugatedMatrix( matrix ):
    row, col = len( matrix ), len( matrix [ 0 ] )

    for i in range( row ):
        for j in range( col ):
            matrix[ i ][ j ] = conjugated( matrix[ i ][ j ] )

    return matrix

def adjointMatrix( matrix  ):
    answ  = conjugatedMatrix( transpMatrix( matrix  ) )
    return answ

def traceMatrix( matrix ):
    answ = [0 , 0]

    row = len( matrix )
    for i in range( row ):
        answ =  suma( matrix[ i ][ i ], answ )
        
    return answ

def internalProduct( matrix1 , matrix2 ):
    
    asnw = traceMatrix( multiplicaMat( transpMatrix( matrix1 ), matrix2,0 ) )


def actionMatrixOnVector( matrix, vector ):
    row, col  = len( matrix ), len( matrix [ 0 ] )
    length = len( vector )

    if  ( col == length ):
        answ = [ [ 0, 0 ] for x in range( row ) ]

        for i in range( row ):
            for j in range( col ):
                
                mult = multComplexNumber( matrix[ i ][ j ], vector[ j ]  )
                answ[ i ] = suma( answ[ i ], mult )
                
        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")
                
    
    
    
         
def normMatrix( matrix  ):
    #revisar
    answ  = multiplicaMat( adjointMatrix( matrix ) , matrix )
    return math.sqrt( traceMatrix( answ )[ 0 ] )



def distMatrix( matrix1, matrix2 ):
    
    answ = normMatrix( matrix1 - matrix2 )
    return answ    

def isUnitary( matrix ):
    row, col = len( matrix ), len( matrix[ 0 ] )
    
    if row == col :
        adjoint = adjointMatrix( matrix )
        print(  multiplicaMat( adjoint , matrix ) )
        print(   multiplicaMat( matrix , adjoint ))
        return multiplicaMat( adjoint , matrix )  == multiplicaMat( matrix , adjoint )
        
        
        

def isHermitan( matrix ):
    answ = adjointMatrix ( matrix  )

    return  str( answ ) == str( matrix )

def tensorProduct( matrix1, matrix2 ):
    fil1 ,col1 = len( matrix1 ), len( matrix1[ 0 ] )
    fil2 ,col2 = len( matrix2 ), len( matrix2[ 0] )

    size = fil1 * fil2
    
    if ( type( matrix1[ 0 ][ 0 ] ) is int   and  type( matrix2[ 0 ][ 0 ] ) is int ):
        answ = [ ]
        pos = 0

        for i in range( fil1 ):
            for j in range( fil2 ):
                answ.append(multComplexNumber( matrix1[ i ], matrix2[ j ] ) )
                
        return answ 
                
    
    elif (  ( fil1 == col1) and ( fil2 == col2 ) ):
        
        answ = [ [ [ 0,0 ] for x in range( size ) ]for x in range( size ) ]
        
        for i in range( size ):
            for j in range( size ):
                answ[ i ][ j ] = multComplexNumber( matrix1[ i//fil1 ][ j//fil2 ] ,
                                                    matrix2[ i % fil1 ][ j % fil2 ] )

        return answ

def circuit():
    o = [ [ 1,0 ], [ 0, 0 ]]

    oo = tensorProduct( o, o )
    X = [ [ [0,0], [1,0] ],[ [1,0], [0,0] ] ]
    H = multiEscalMat( [1/ math.sqrt(  2 )  ,0]  , [ [ [1,0], [1,0] ], [ [1,0], [-1,0] ] ] )

    
    M1 = tensorProduct( X, H )
    M2 = tensorProduct( H, H )

    M3 = actionMatrixOnVector( M1, oo )

    y = actionMatrixOnVector( M2, M3 )
    print( y )
circuit()

"""
def main():
    a = [1,1]
    b = [0,0]
    c = [0,0]
    d = [1,-1]
    matrix = [[a,b],[c,d]]
    print( matrix )
    print( isHermitan(  matrix ) ) 
    print( isUnitary( matrix ) )
main()
"""
