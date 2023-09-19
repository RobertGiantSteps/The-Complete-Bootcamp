# *****************
# UN JUEGO AL TENIS
# *****************


def run(points: str) -> str:
    player1 = 0
    player2 = 0
    winner = None
    for point in points[:]:
        if point == 'A':
            player1 += 1           
        else:
            player2 += 1                
    if player1 > player2:
        winner = 'A'
    else:
        winner = 'B'
        
    winner = winner

    return winner


if __name__ == '__main__':
    run('ABAABA')