import math 
import unittest
from complexNumberLibrary import *

class TestLibComplex(unittest.TestCase):
    def testSuma(self):
        a, b = [ 3, -1 ],  [ 1, 4 ]
        c, d = [ 6, 7 ], [ 6, 6 ]
        e, f = [ 8, 9 ], [ 2, 1 ]
        
        self.assertEqual( suma( a, b ), [ 4, 3  ] )
        self.assertEqual( suma( c, d ), [ 12, 13 ] )
        self.assertEqual( suma( e, f ), [ 10, 10 ] )
        
    def testSub(self):
        a, b = [ 5, 8 ], [ 1, 2 ]
        c, d = [ 6, 7 ], [ 6, 6 ]
        e, f = [ 8, 9 ], [ 2, 1 ]
        
        self.assertEqual( sub( a, b ), [ 4, 6 ] )
        self.assertEqual( sub( c, d ), [ 0, 1 ] )
        self.assertEqual( sub( e, f ), [ 6, 8 ] )
        
    def testMult(self):
        a, b = [ 3, -1 ], [ 1, 4 ]
        c, d = [ 6, 7 ], [ 6, 6 ]
        e, f = [ 8, 9 ], [ 2, 1 ]
        
        self.assertEqual( multComplexNumber( a, b ), [ 7, 11 ] )
        self.assertEqual( multComplexNumber( c, d ), [ -6, 78 ] )
        self.assertEqual( multComplexNumber( e, f ), [ 7, 26 ] )

    def testDiv(self):
        a, b = [ 3, 2 ], [ -1, 2 ]
        c, d = [ 6, 7 ], [ 6, 6 ]
        e, f = [ 8, 9 ], [ 2, 1 ]
        
        self.assertEqual( divComplexNumber( a, b ), [ 0.2, -1.6 ] )
        self.assertEqual( divComplexNumber( c, d ), [ 1.0833333333333333, 0.08333333333333333 ] )
        self.assertEqual( divComplexNumber( e, f ), [ 5, 2 ] )
        

    def testConjugated(self):
        a = [ 1, -1 ]
        b = [ 8 , -3 ]
        c = [ 9 , -2 ]
        
        self.assertEqual( conjugated( a  ), [ 1, 1 ]  )
        self.assertEqual( conjugated( b  ), [ 8, 3 ]  )
        self.assertEqual( conjugated( c  ), [ 9, 2 ]  )

        
    def testModule(self):
        a = ( 1, -1 )
        b = ( 8 , -3 )
        c = ( 9 , -2 )
        
        self.assertEqual( module( a ) , math.sqrt( 2 ) )
        self.assertEqual( module( b ) , 8.54400374531753 )
        self.assertEqual( module( c ) , 9.219544457292887  )
        
    def testCartesian( self ):
        a = [ 5 , 5 ]
        b = [ -5, 5 ]
        c = [ -5 , -5 ]
        d = [ 5 , -5 ]
        
        self.assertEqual( cartesianToPolar( a ) ,[  5* math.sqrt( 2 ), math.radians( 45 ) ])
        self.assertEqual( cartesianToPolar( b ) ,[  5* math.sqrt( 2 ), math.radians( 135 ) ])
        self.assertEqual( cartesianToPolar( c ) ,[  5* math.sqrt( 2 ), math.radians( 225 ) ])
        self.assertEqual( cartesianToPolar( d ) ,[  5* math.sqrt( 2 ), math.radians( 315 ) ])

    def testPhase( self ):
        self.assertEqual( phase( [1,1] ), 0.7853981633974483 )
        self.assertEqual( phase( [-1,1] ), 2.356194490192345 )
        

if __name__ == '__main__':
    unittest.main()
