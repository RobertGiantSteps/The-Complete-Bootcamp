"""
Escriba un programa en Python que acepte dos valores enteros (𝑥 e 𝑦) que 
representarán un punto (objetivo) en el plano. 
El programa simulará el movimiento de un «caballo» de ajedrez moviéndose 
de forma alterna: 2 posiciones en 𝑥 + 1 posición en 𝑦. 
El siguiente movimiento que toque sería para moverse 1 posición en 𝑥 + 2 posiciones 
en 𝑦.El programa deberá ir mostrando los puntos por los que va pasando el «caballo» 
hasta llegar al punto objetivo (solución).

        Entrada: objetivo_x=7; objetivo_y=8;

        Salida: (0, 0) (1, 2) (3, 3) (4, 5) (6, 6) (7, 8)



"""

point_x = 7
point_y = 8
horse_move = (0,0)
x_axis,y_axis = horse_move

if point_x < point_y:
        for move in range(point_y - 2):
                if x_axis == y_axis:
                        move = f'({x_axis},{y_axis})'
                        x_axis += 1
                        y_axis += 2
                elif x_axis < y_axis:
                        move = f'({x_axis},{y_axis})'
                        x_axis += 2
                        y_axis += 1
                print(move,end=' ')
else:
        for move in range(point_x - 2):
                if x_axis == y_axis:
                        move = f'(🎠{x_axis},{y_axis})'
                        x_axis += 1
                        y_axis += 2
                elif x_axis < y_axis:
                        move = f'(🎠{x_axis},{y_axis})'
                        x_axis += 2
                        y_axis += 1
                print(move,end=' ')

print()
print('----------------------------------------------------------')                
x = 7
y = 8
counter = 0
limit = x - 2
x = 0
y = 0

while  counter <= limit:
        if x == y:
                horse_atack = f'({x},{y})'
                x += 1
                y += 2
        else:
                horse_atack = f'({x},{y})'
                x += 2
                y += 1
        print(horse_atack,end=' ')
        counter += 1
        

print()
print('----------------------------------------------------------')       
                
# =================================================
# OPCIÓN A
# =================================================
TARGET_X = 7
TARGET_Y = 8

horse_x = 0
horse_y = 0
print(f'({horse_x}, {horse_y})', end=' ')

flow = True  # Asignamos True a la variable flow
while horse_x != TARGET_X and horse_y != TARGET_Y:
    if flow:
        horse_x += 1
        horse_y += 2
    else:
        horse_x += 2
        horse_y += 1
    print(f'({horse_x}, {horse_y})', end=' ')
    flow = not flow # Invertimos el valor de flow, ahora flow será False en este caso para alternar entre True y False
    
    # En este caso, el valor de flow se invertirá dependiendo de su valor inicial.


# =================================================
# OPCIÓN B
# =================================================
TARGET_X = 7
TARGET_Y = 8

horse_x = 0
horse_y = 0

flow = True
while horse_x <= TARGET_X and horse_y <= TARGET_Y:
    print(f'({horse_x},{horse_y})')
    horse_x += 2 - flow
    horse_y += 1 + flow
    flow = not flow               
                        
                        
                        





        
        
        


        
       
        
                

       


