"""

Escriba un programa que calcule la distancia hamming entre dos cadenas de texto 
de la misma longitud (solución).

        Entrada: 0001010011101 y 0000110010001

        Salida: 4

"""
hamming = 0

code_block1 = '2143896'
code_block2 = '2233796'
code_length = len(code_block1)


for bit in range(code_length):
    if not code_block1[bit] == code_block2[bit]:
        hamming += 1
    else:
        continue
print(f'Hamming distance: {hamming}')

print()
print('---------------------------------------------')

# Solución

str1 = '0001010011101'
str2 = '0000110010001'

distance = 0

# Suponemos que ambas cadenas tienen la misma longitud
for i in range(len(str1)):
    if str1[i] != str2[i]:
        distance += 1
print(distance)


    
    