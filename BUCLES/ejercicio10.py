"""
Escriba un programa que muestre por pantalla todas las fichas del dominó. 
La ficha «en blanco» se puede representar con un 0 (solución).

0|0 0|1 0|2 0|3 0|4 0|5 0|6
1|1 1|2 1|3 1|4 1|5 1|6
2|2 2|3 2|4 2|5 2|6
3|3 3|4 3|5 3|6
4|4 4|5 4|6
5|5 5|6
6|6



"""
max_domino = 6
minimun_limit = 0

for blue in range(max_domino + 1):
    for red in range(minimun_limit,max_domino + 1):        
        if red == max_domino:
            print(f'{blue}|{red}',end=' ')
            print()
        elif blue > red:
            red = blue
            print(f'{blue}|{red}',end=' ')
            red += 1
        elif red > blue:
            print(f'{blue}|{red}',end=' ')            
        else:
            print(f'{blue}|{red}',end=' ')
    max_domino -= 1
    minimun_limit += 1
    max_domino += 1
    

print('-------------------------------------------------------------------')
   
# Solución

MAX_DOMINO = 6

for up_part in range(MAX_DOMINO + 1):
    for down_part in range(up_part, MAX_DOMINO + 1):
        domino = f'{up_part}|{down_part}'
        print(domino, end=' ')
    print()
             
           
            
    

    
           
   