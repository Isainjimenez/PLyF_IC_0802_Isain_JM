valores = [2,4]

#print('-----------------------------------------------------> S U M A <-----------------------------------------------------')

#print('==> Suma de los numeros 2+4')
#valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]

from functools import reduce
suma = reduce(lambda x, y: x + y, valores)
print('El resultado = ' , suma)

#print('-------------------------------------------> M U L T I P L I C A C I O N <-------------------------------------------')

#print('==> Multiplicacion de 2x4')

#from functools import reduce
multi = reduce(lambda x, y: x * y, valores)
print('El resultado = ' , multi)
#def multiplicar_por (n):
 # return lambda x: x * n

#duplicar = multiplicar_por(2)
#triplicar = multiplicar_por(3)
#diez_veces = multiplicar_por(10)

#print(duplicar(4))
#print(triplicar(9))
#print(diez_veces(11))

#print('-------------------------------------------------> D I V I C I O N <-------------------------------------------------')

#print('==> Divicion de 2/4')

#from functools import reduce
divi = reduce(lambda x, y: x / y, valores)
print('El resultado = ' , divi)

#print('----------------------------------------------------> R E S T A <----------------------------------------------------')

#print('==> Resta de los numero 2-4')
#valores = [100, 25]
#from functools import reduce
resta = reduce(lambda x, y: x - y, valores)
print('El resultado = ' , resta)

#print('----------------------------------------------------> M O D U L O <----------------------------------------------------')

#from functools import reduce
porc = reduce(lambda x, y: x % y, valores)
print('El resultado = ' , porc)
#la función reduce(). Esta función se utiliza principalmente para llevar a cabo un cálculo acumulativo sobre una lista de valores y devolver el resultado.