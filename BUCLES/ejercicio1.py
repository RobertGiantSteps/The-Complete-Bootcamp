"""
Escriba un programa que encuentre la mínima secuencia 
de multiplos de 3 (distintos) cuya suma 
sea igual o superior a un valor dado 

Entrada: 45

Salida: 0, 3, 6, 9, 12, 15

Un número es múltiplo de 3 cuando es el resultado de multiplicar 3
por otro número. 15 es múltiplo de 3, ya que resulta de multiplicar 3 por 5.


"""

value = 45 

secuence = 0


for num in range(value):
    multiples = num * 3 # 0, 3,
    secuence += multiples  
    if secuence <= value:
        print(f'{multiples}, ',end='')

print()

# Solución: 

total_sum = 45
current_sum = 0
current_3mult = 0
print(f'M={current_3mult:2d}: S={current_sum:2d}')

while current_sum < total_sum:
    current_3mult += 3
    current_sum += current_3mult
    print(f'M={current_3mult:2d}: S={current_sum:2d}')


         

        
        
    
        