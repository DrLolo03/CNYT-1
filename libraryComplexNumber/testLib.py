import unittest
from lib import *

class TestLibComplex(unittest.TestCase):
    def testSuma(self):
        a = ( 3, -1 )
        b = ( 1, 4 )
        self.assertEqual( suma( a, b ), ( 4, 3 ) )

    def testSub(self):
        a = ( 5, 8 )
        b = ( 1, 2 )
        self.assertEqual( sub( a, b ), ( 4, 6 ) )

    def testMult(self):
        a = ( 3, -1 )
        b = ( 1, 4 )
        self.assertEqual( multComplexNumber( a, b ), ( 7, 11 ) )

    def testDiv(self):
        a = ( -2, 1 )
        b = ( 1, 2 )
        self.assertEqual( divComplexNumber( a, b ), ( 0, 1 ) )

    def testConjugated(self):
        a = ( 1, -1 )
        self.assertEqual( conjugated( a  ), ( 1, 1 )  )
        
    def testModule(self):
        a = ( 1, -1 )
        self.assertEqual( module( a ) , math.sqrt( 2 ) )

    def testCartesian( self ):
        a = ( 1 , 1)
        self.assertEqual( cartesianToPolar( a ) ,( math.sqrt( 2 ),45) )

    
        
        

if __name__ == '__main__':
    unittest.main()
