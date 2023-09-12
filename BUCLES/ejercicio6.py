"""

Escriba un programa en Python que acepte dos cadenas de texto y compute el 
producto cartesiano letra a letra entre ellas (solución).

        Entrada: str1=abc; str2=123

        Salida: a1 a2 a3 b1 b2 b3 c1 c2 c3
        
        
Supongamos que tienes dos conjuntos A y B:

A = {a, b, c}
B = {1, 2}

Para calcular el producto cartesiano de estos dos conjuntos,
simplemente combinas cada elemento de A con cada elemento de B 
de la siguiente manera:

A × B = {(a, 1), (a, 2), (b, 1), (b, 2), (c, 1), (c, 2)}        

"""
# Con tuplas:

str1='jazz'
to_tuple = tuple(str1)

str2='1234'
to_tuple_number = tuple(str2)


for  letter in range(len(to_tuple)):
    for number in range(1,len(to_tuple_number) + 1):
        print(f'{to_tuple[letter]}{number}',end=' ')


print('----------------------------------------------------------')

# Con str[índice]
        
string1 = 'abcde'
string2 = '12345'

for char1 in range(len(string1)):
    for char2 in range(len(string2)):
        print(f'{string1[char1]}{string2[char2]}',end=' ')
        

print('-----------------------------------------------------------')

        
# Solución:

str1 = 'abc'
str2 = '123'

for char1 in str1:
    for char2 in str2:
        print(f'{char1}{char2}', end=' ')


        
        
        

      



