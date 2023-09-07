"""
Escriba un programa en Python que realice las siguientes 9 multiplicaciones. 
¿Nota algo raro en el resultado? (solución)

                     1 * 1
                    11 * 11
                   111 * 111
                       *
                       *
                       *
            111111111  *  111111111 
            
        an​=10n

Potencias de 10

Por ejemplo:

    a0=100=1
    a1=101=10
    a2=102=100
    a3=103=1000
    a4=104=10000
    a5=105=100000
    a6=106=1000000         



"""

EXPONENT = 10
multiplying = 1
multiplier = 1


for power in range(1,10):
    multiplication = multiplying * multiplier
    print(f'{multiplying} * {multiplier} = {multiplication}')
    power_of_ten = EXPONENT ** power # , 10, 121, 
    multiplying += power_of_ten
    multiplier += power_of_ten

print()
   
# Solucion:

one = '1'
for i in range(1, 10):
    factor = int(one * i) # 1, 11, etc ... 
    result = factor * factor # 1, 121, etc ... 
    print(f'{factor} · {factor} = {result}') # 1 * 1 = 1

            
    
    
    
        
  
    
    
    
    