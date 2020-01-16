import unittest
from lib import *

class TestLibComplex(unittest.TestCase):
    def testSuma(self):
        a = ( 5, 8 )
        b = ( 1, 2 )
        self.assertEqual( suma( a, b ), ( 6, 10 ) )
        
        

if __name__ == '__main__':
    unittest.main()
