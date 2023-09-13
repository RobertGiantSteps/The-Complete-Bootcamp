"""

Escriba un programa que calcule el máximo común divisor entre dos números enteros. 
No utilice ningún algoritmo existente. 
Hágalo probando divisores (solución).

        Entrada: a=12; b=44

        Salida: 4
A continuación, te mostraré un ejemplo para calcular el MCD de 48 y 18 
utilizando el algoritmo de Euclides:

    Comenzamos con a = 48 y b = 18.
    Dividimos 48 por 18: r = 48 % 18 = 12.
    Como r no es igual a cero, reemplazamos a por 18 y b por 12.
    Repetimos el proceso: r = 18 % 12 = 6.
    Continuamos: r = 12 % 6 = 0.
    Ahora que r es igual a cero, el MCD de 48 y 18 es 6.

"""

a = 12
b = 44

rest_division = a % b

while rest_division != 0:
    a = b
    b = rest_division
    rest_division = a % b
print(f'MCD = {b}')


print('-------------------------------------------------')

# Solución 

a = 12
b = 44

if a < b:
    _min = a
else:
    _min = b

for divisor in range(_min, 0, -1):
    if a % divisor == 0 and b % divisor == 0:
        mcd = divisor
        break
else:
    mcd = 1

print(mcd)