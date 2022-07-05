suma = [5, 5, 5]
suma2 = [10,10]
cadena = "3.- Isain"

import Principal  
from functools import reduce
import string


s = reduce(lambda x, y: x + y, suma )
print ('1.- El resultado es: ', s)

s = reduce(lambda x, y:  x + y, suma2 )
print ('2.- El resultado es: ', s)

s = reduce(lambda x, y: x + y ,Principal.x)
print (s)

s = reduce(lambda x , y: x + y ,Principal.cadena)
print ('La cadena es: ', s)

s = reduce(lambda x, y: x + y , Principal.valu2)
print ('4.- El resultado es: ', s)

s = reduce(lambda x, y: x + y , Principal.valu)
print ('5.- El resultado es: ', s)

s = reduce(lambda x, y: x + y, Principal.valu )
print ('6.- El resultado es: ', s)
