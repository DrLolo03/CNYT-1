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
        a = ( 3, 2 )
        b = ( -1, 2 )
        self.assertEqual( divComplexNumber( a, b ), ( 0.2, -1.6 ) )
        

    def testConjugated(self):
        a = ( 1, -1 )
        self.assertEqual( conjugated( a  ), ( 1, 1 )  )

        
    def testModule(self):
        a = ( 1, -1 )
        self.assertEqual( module( a ) , math.sqrt( 2 ) )

    def testCartesian( self ):
        a = ( 5 , 5 )
        b = ( -5, 5 )
        c = ( -5 , -5 )
        d = ( 5 , -5 )
        
        self.assertEqual( cartesianToPolar( a ) ,( 5 * math.sqrt( 2 ), 45 ) )
        self.assertEqual( cartesianToPolar( b ) ,( 5 * math.sqrt( 2 ), 135 ) )
        self.assertEqual( cartesianToPolar( c ) ,( 5 * math.sqrt( 2 ), 225 ) )
        self.assertEqual( cartesianToPolar( d ) ,( 5 * math.sqrt( 2 ), 315 ) )
        
        

if __name__ == '__main__':
    unittest.main()
