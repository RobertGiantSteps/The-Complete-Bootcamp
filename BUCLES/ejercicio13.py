
"""
Escriba un programa que permita al usuario adivinar un número. Indicar si el número buscado es menor o mayor que el que se está preguntando y 
mostrar igualmente el número de intentos hasta encontrar el número objetivo (solución):

Introduzca número: 50
Mayor
Introduzca número: 100
Menor
Introduzca número: 90
Menor
Introduzca número: 87
✅ ¡Enhorabuena! Has encontrado el número en 4 intentos

"""

import random

goal_number = 0
counter = 0
success = 55

while goal_number != success:
    goal_number  = int(input('Introduzca número: '))
    if goal_number > success:
        msg = 'Menor'
    else:
        goal_number < success
        msg = 'Mayor'
    counter += 1
    print(msg)
else:
    msg = f'✅ ¡Enhorabuena! Has encontrado el número en {counter} intentos'
    print(msg)
    
    
print('-------------------------------------------------')

goal_number = 0
counter = 0
success = random.randint(0,100)

while goal_number != success:
    goal_number  = int(input('Introduzca número: '))
    if goal_number > success:
        msg = 'Menor'
    else:
        goal_number < success
        msg = 'Mayor'
    counter += 1
    print(msg)
else:
    msg = f'✅ ¡Enhorabuena! Has encontrado el número en {counter} intentos'
    print(msg)
    
    
    
    
    
# Solución: 

TARGET_NUMBER = 87

num_tries = 0
while True:
    number = int(input('Introduzca número: '))
    num_tries += 1
    if number > TARGET_NUMBER:
        print('Menor')
    elif number < TARGET_NUMBER:
        print('Mayor')
    else:
        print(f'✅ ¡Enhorabuena! Has encontrado el número en {num_tries} intentos')
        break
    
        
            
    