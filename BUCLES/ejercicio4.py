"""


Escriba un programa en Python que acepte una cadena de texto e indique si todos 
sus caracteres son alfabéticos. No usar la función isalpha() sino una constante 
ALPHABET = 'abcdefghijklmnopqrstuvwxyz' (solución)

        Entrada: hello-world

        Salida: Se han encontrado caracteres no alfabéticos

"""

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

text = 'hello world'
corrected_text = text.lower()
space = ' '


for letter in corrected_text:
    if letter not in  ALPHABET and letter != space:
        msg = f'Non-alphabetic char found! " {letter} "'
        break
                  
    else:
        msg = f'All chars are alphabetic: {corrected_text}'

print(msg)

print('-------------------------------------------------------------')

# Solucion 

ext = 'hello-world'

for char in text:
    if not char.isalpha():
        print('Non-alphabetic char found!')
        break
else:
    print('All chars are alphabetic')

