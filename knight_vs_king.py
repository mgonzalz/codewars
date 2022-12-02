knight_position = (1, 'a')
king_position = (3, 'c')
def knight_vs_king (knight_position, king_position):
    #Three possible outputs are "Knight", "King", and "None"
    (x, y) = knight_position #posición knignt
    (a, b) = king_position #posición king
    dist_x = x - a #distancia eje x
    dist_y = ord(y) - ord(b) #ord pasa la letra a número en ASCII
    superf = (dist_x**2) + (dist_y**2) #superficie
    if superf == 5:
        return "Knight"
    elif superf <= 2:
        return"King"
    else:
        return"None"
if __name__ == "__main__":
    knight_vs_king(knight_position, king_position)
