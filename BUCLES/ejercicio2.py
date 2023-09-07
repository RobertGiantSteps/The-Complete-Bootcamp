"""
Escriba un programa que pida nombre y apellidos de una persona 
(usando un solo input) y repita la pregunta mientras el nombre no esté en formato título (solución).

¿Su nombre? ana torres blanco
Error. Debe escribirlo correctamente
¿Su nombre? Ana torres blanco
Error. Debe escribirlo correctamente
¿Su nombre? Ana Torres blanco
Error. Debe escribirlo correctamente
¿Su nombre? Ana Torres Blanco


"""

name_format = False

while name_format == False:
    name = input('¿Su nombre? ')
    name_size = len(name)
    if name_size < 2 or name != name.title():
        print(f'{name} Error vuelve a intentarlo: ')    
    else:
        print('Formato correcto, Gracias y buen día')
        name_format = True
        
        
 #OPCIÓN A
while True:
    name = input('¿Su nombre? ')
    if name.istitle():
        break
    print('Error. Debe escribirlo correctamente')

# OPCIÓN B (ESTA ES LA TIPA)
while not (name := input('¿Su nombre? ').istitle()): # Mientras not (etc...)
    print('Error. Debe escribirlo correctamente')
        