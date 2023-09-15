"""
Escriba un programa que calcule el valor de 𝑥 para el que la función 𝑓(𝑥)=𝑥2−6𝑥+3 
obtiene su menor resultado. 
Centre la búsqueda en el rango [−9,9]

    sólo con valores enteros (solución).

El resultado es: 𝑥=3 y 𝑓(𝑥)=−6

"""




minimum_f = None

for x in range(-9,9):
    func1 = (x ** 2)
    func2 = 6 * x
    function = func1 - func2 + 3
    if minimum_f is None or function < minimum_f:
        minimum_x = x
        minimum_f = function 
print(f'En x = {minimum_x} la función f(x) alcanza el valor mínimo de {minimum_f}')
    
print('-------------------------------------------------------------------')
# Resultado:

min_f = None
for x in range(-9, 9):
    f = x**2 - 6 * x + 3
    if min_f is None or f < min_f:
        min_x = x
        min_f = f

print(f'x = {min_x}; f(x) = {min_f}')


