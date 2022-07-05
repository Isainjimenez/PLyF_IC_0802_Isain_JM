#No hay sobrecarga de métodos en python. 
#|<--------------------><--------------------><--------------------><--------------------><--------------------><-------------------->|
#|                                                                                                                                    |
#|                                                                                                                                    |
#|                                    C r e a d o   p o r :   I s a i n   J i m e n e z   M a r t i n e z                             |
#|                                                                                                                                    |
#|                                                                                                                                    |
#|<--------------------><--------------------><--------------------><--------------------><--------------------><-------------------->|

from functools import reduce


class Base(): 


    def add(self,a,b):
        self.a=a
        self.b=b

        suma = reduce(lambda a: a * b, add_fun_1.add)
        print (suma)

class Derived(Base): 
    def add(self,a,b):
        self.a=a
        self.b=b 
        suma = reduce(lambda a: a - b, add_fun_2.add)
        print (suma)



add_fun_1=Base() 
add_fun_2=Derived()

add_fun_1.add(4,5) 
add_fun_2.add(4,2)   