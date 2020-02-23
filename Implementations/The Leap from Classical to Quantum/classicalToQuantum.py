from sys import stdin
import math

def valid( phase, solp):

        for x in range( phase ):
                if ( ( abs( x - phase ) == abs( solp[x] - solp[phase] ) ) or ( solp[ phase ] == solp[x] ) ):
                        return False
        
        return True

def backTracking( size, phase, solp ):
        if phase < size :
                for x in range( size ):
                        solp[ x ] = x
                        mSolp = solp[ : ]
                        
                        if valid( phase, mSolp[:]):
                                
                                if phase < size - 2:
                                        
                                        backTracking( size, phase + 1, mSolp[:])
                                else:
                                        print( mSolp )
def main():
        n = int( stdin.readline().strip() )
        backTracking( n, 0, [ 0 for x in range( n ) ] )    
main()
