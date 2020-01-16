
"""
numero asociado a la entrada de print
1) suma
2) resta
3) mult
4) div
5) conjugado
6) modulo
7) cartesianos -> polar
8) retornar fase
"""

import math 
class complexNumber:
    def print( self, complexNumber ):
        print( complexNumber ) 

    def sumComplexNumber( self, complexNumber1, complexNumber2 ):
        answ = ( complexNumber1[ 0 ] + complexNumber2[ 0 ],
                 complexNumber1[ 1 ] + complexNumber2[ 1 ] )
        
        self.print( answ )

    def subtractComplexNumber( self, complexNumber1, complexNumber2 ):
        answ = ( complexNumber1[ 0 ] - complexNumber2[ 0 ],
                 complexNumber1[ 1 ] - complexNumber2[ 1 ] )
        
        self.print( answ )

    def multComplexNumber( self, complexNumber1, complexNumber2 ):
        answ = ( complexNumber1[ 0 ] * complexNumber2[ 0 ] - complexNumber1[ 1 ] * complexNumber2[ 1 ],
                  complexNumber1[ 1 ] * complexNumber2[ 0 ] + complexNumber1[ 0 ] * complexNumber2[ 1 ])
        
        self.print( answ )

    def divComplexNumber( self, complexNumber1, complexNumber2 ):
        div = complexNumber2[0]**2 + complexNumber2[1]**2
        
        try :
            answ =( ( complexNumber1[ 0 ] * complexNumber2[ 0 ] + complexNumber1[ 1 ] * complexNumber2[ 1 ] )/div,
                   ( complexNumber1[ 0 ] * complexNumber2[ 0 ] - complexNumber1[ 1 ] * complexNumber2[ 1 ] ) /div )

            self.print( answ )
            
        except ZeroDivisionError as error :
            print('Se produjo el siguiente error',error)
        
    def conjugated( self, complexNumber ):
        answ = ( complexNumber[ 0 ], 
                 -complexNumber[ 1 ] )

        self.print( answ )

    def module( self, complexNumber ):
        answ = math.sqrt( complexNumber[ 0 ]**2 + complexNumber[ 1 ] **2 )
        
        self.print( answ )

    def cartesianToPolar( self, complexnumber ):
        angle = math.atan( complexNumber[ 1 ] / complexNumber[ 0 ] ) 
        answ = ( self.module( complexNumber) ,
                angle )
        
        self.print( answ )        
