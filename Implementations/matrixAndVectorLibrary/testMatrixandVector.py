import unittest
from matrixAndVectorLibrary import *

#complex numbers
a = [ 1,3 ]
b = [ 2,4 ]
c = [ 6,5 ]
d = [ 4, 9 ]



class TestLibComplex(unittest.TestCase):
    
    def testSumVect(self):
        
        self.assertEqual( sumVect( [ a, b ], [a ,b ] ),
                          [[2, 6], [4, 8]] )
        
        self.assertEqual( sumVect( [ a, c ], [c ,b ] ),
                          [[7, 8], [8, 9]] )
    
    def testInverseVect(self):
        
        self.assertEqual( inverseVect( [ a, c ] ),
                          [[-1, -3], [-6, -5]] )
        
        self.assertEqual( inverseVect( [ b, a ] ),
                          [[-2, -4], [-1, -3]] )
        
        
    def testEscalVect(self):

        self.assertEqual( escalVect ( [ a, b ],b  ),
                          [[-10, 10], [-12, 16]] )
        
        self.assertEqual( escalVect ( [ b, c ], c ),
                          [[-8, 34], [11, 60]] )
        

    def testSumMat(self):

        self.assertEqual( sumMat( [ [ a,a ],[ b,b ] ] ,
                                  [ [ b,a ],[ a,b ] ] ), [[[3, 7], [2, 6]], [[3, 7], [4, 8]]] )
        
        self.assertEqual( sumMat( [ [ c,a ],[ a,b ] ] ,
                                  [ [ b,c ],[ b,b ] ] ), [[[8, 9], [7, 8]], [[3, 7], [4, 8]]] )
        

    def testInverseMat(self):

        self.assertEqual( inverseMat( [[a],[b],[c]] ),
                          [[[-1, -3]], [[-2, -4]], [[-6, -5]]] )
        
        self.assertEqual( inverseMat( [[a,a,c],[c,b,a],[d,c,b]] ),
                          [[[-1, -3], [-1, -3], [-6, -5]], [[-6, -5], [-2, -4], [-1, -3]], [[-4, -9], [-6, -5], [-2, -4]]] )
        
        
    def testMultiEscalMat(self):

        self.assertEqual( multiEscalMat( d , [ [ c,a ],[ a,d ] ] ),
                          [[[-21, 74], [-23, 21]], [[-23, 21], [-65, 72]]] )
        
        self.assertEqual( multiEscalMat( c, [ [ a,a ],[ b,b ] ] ),
                          [[[-9, 23], [-9, 23]], [[-8, 34], [-8, 34]]] )

        

    def testTranspMatrix( self ):

        self.assertEqual( transpMatrix( [ [ b,a,a ],[ a,b,a ] ] ),
                          [[[2, 4], [1, 3]], [[1, 3], [2, 4]], [[1, 3], [1, 3]]] )
        
        self.assertEqual( transpMatrix( [ [ a,b, c],[ c,b,a ] ] ),
                          [[[1, 3], [6, 5]], [[2, 4], [2, 4]], [[6, 5], [1, 3]]] )
        

    def testConjugatedMatrix( self ):
        self.assertEqual( conjugatedMatrix( [ [ b,a,c ],[ c,b,d ] ] ),
                          [[ [2, -4], [1, -3], [6, -5] ], [ [6, -5], [2, -4], [4, -9] ] ] )
        
        self.assertEqual( conjugatedMatrix( [ [ a,b, c],[ c,b,a ] ] ),
                          [[ [1, -3], [2, -4], [6, -5]], [[6, -5], [2, -4], [1, -3]] ] )
        
        
    def testAdjointMatrix( self ):
        
        self.assertEqual( adjointMatrix( [ [ b,a,a ],[ a,b,a ] ] ),
                          [[[2, -4], [1, -3]], [[1, -3], [2, -4]], [[1, -3], [1, -3]]] )
        
        self.assertEqual( adjointMatrix( [ [ a,b, c],[ c,b,a ] ] ),
                          [[[1, -3], [6, -5]], [[2, -4], [2, -4]], [[6, -5], [1, -3]]] )

    def testMultiplicaMat( self ):

        self.assertEqual( multiplicaMat( [ [ a,a ],[ b,b ] ] , [ [ b,a ],[ a,b ] ] ),
                          [[[-18, 16], [-18, 16]], [[-22, 26], [-22, 26]]] )
        
        self.assertEqual( multiplicaMat( [ [ a,a,b],[ b,b,a ] ] , [ [ b,a ],[ a,b ],[b,b] ] ),
                          [[[-30, 32], [-30, 32]], [[-32, 36], [-32, 36]]] )

    def actionMatrixOnVector( self ):
        a = [ 1,4 ]
        b = [ 4, 0 ]
        c = [ 7, -1 ]
        d = [ 0 ,1 ]
        e = [ 5, 6]
        
        self.assertEqual( actionMatrixOnVector( [[ a, c, d],[ b, c ,b],[ d, b, e]], [ e, d, c] ),
                          [[-17, 40], [49, 27], [35, 46]] )
        
    
    def testNormVector( self ):
        a, b = [ 3, 0 ], [ -6, 0 ]
        c = [ 2, 0 ]

        self.assertEqual( normVector( [ a, b, c ] ), math.sqrt( 49 )  )
        


    def testDistVector( self ) :
        a, b = [ 3, 0 ], [ 1, 0 ]
        c, d = [ 2, 0 ], [ -1,0 ]

        self.assertEqual( distVector( [ a, b, c ],[ c ,c, d] ), math.sqrt( 11 )  )
        
        

    def testIsUnitary( self ):
        a, b = [ 1,0 ], [ 0, 0 ]
        c = [ 0, 1 ]

        self.assertEqual( isUnitary([ [ c , b], [ b, c ] ]),
                          True )
        
        self.assertEqual( isUnitary([ [ a ,b ], [ b, a ] ]),
                          True )
        
        

    def testIsHermitan( self ):
        a = [ 7,0 ]
        b = [ 6,5 ]
        c = [ 6, -5 ]
        d = [ -3, 0 ]

        e, f = [ 1,0], [ 0, 0]
        
        self.assertEqual( isHermitan([[ a, b ], [c, d ] ] ),
                          True )
        
        self.assertEqual( isHermitan([ [ e ,f ], [ f, e ] ]),
                          True )
        

    def testTensorProduct( self ):
        matrix1 = [[2,0],[3,0]]
        matrix2 = [[4,0],[6,0],[3,0]]
        
        self.assertEqual( tensorProduct( matrix1 ,matrix2 ),
                          [[8, 0], [12, 0], [6, 0], [12, 0], [18, 0], [9, 0]] )


        matrix1 = [ [ [1, 0], [2,0] ], [ [0,0 ] ,[1,0] ]]
        matrix2 = [ [ [3, 0], [2,0] ],[ [-1,0 ] ,[0,0] ]]
        
        self.assertEqual( tensorProduct( matrix1 ,matrix2 ),
                          [[[3, 0], [2, 0], [6, 0], [4, 0]], [[-1, 0], [0, 0], [-2, 0], [0, 0]], [[0, 0], [0, 0], [3, 0], [2, 0]], [[0, 0], [0, 0], [-1, 0], [0, 0]]] )

if __name__ == '__main__':
    unittest.main()
