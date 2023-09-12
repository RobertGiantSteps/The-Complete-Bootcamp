"""
Escriba un programa en Python que acepte un número entero 𝑛
y realice el siguiente cálculo de productos sucesivos (solución):

            ∏𝑖=1𝑛𝑖2=12⋅22⋅32⋅⋯⋅𝑛2


"""

target_number = 5
power = 2
mult = 1

for base in range(1,target_number + 1):
    if base <= target_number:
        exponentiation = base ** power
        mult *= exponentiation
print(f'∏𝑖=1𝑛𝑖2=1^2⋅2^2⋅3^2⋅⋯⋅𝑛2 = {mult}'  )

print('---------------------------------------------')

lucky_number = 5
base_number = 1
exponent = 2
mult_operation = 1

while base_number <= lucky_number:
    exp_operation = base_number ** exponent
    mult_operation *= exp_operation
    base_number += 1
print(f'∏𝑖=1𝑛𝑖2=1^2⋅2^2⋅3^2⋅⋯⋅𝑛2 = {mult}'  )

print('---------------------------------------------')
# Solucion:

n = 5

acc = 1
for i in range(1, n + 1):
    acc *= i ** 2

print(acc)
    


        
    
    