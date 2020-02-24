import unittest
from classicalToQuantum import *



class classicalToQuantum(unittest.TestCase):
    
    def testExperimentBooleanMatrix( self  ):
        booleanMatrix = [[False, False, False, False, False, False], [True, False, False, False, False, True],
                         [True, False, False, False, False, False], [False, False, True, False, False, False],
                         [False, False, False, True, False, False], [False, False, False, False, True, False]]

        vectIni = [True, False, False, False, False, False]

        self.assertEqual(experimentBooleanMatrix( 1 ,booleanMatrix[:], vectIni[:]  ),
                         [False, True, True, False, False, False] )

        self.assertEqual(experimentBooleanMatrix( 3 ,booleanMatrix[:], vectIni[:]   ),
                         [False, False, False, False, True, False] )

        self.assertEqual(experimentBooleanMatrix( 5 ,booleanMatrix[:], vectIni[:]   ),
                         [False, True, False, False, False, False] )

    def testMultipleSlitExperiment( self ):
        pass

    def testMultipleSlitQuantumExperiment( self ):
        pass

    def testGraphProbabilitiesVector( self ):
        pass
        
if __name__ == '__main__':
    unittest.main()
