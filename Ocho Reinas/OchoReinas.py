def celda_libre(fila, col):
    for i in range(8):
        if tablero[fila][i] == 'R' or tablero[i][col] == 'R':
            return False
    if fila <= col:
        c = col - fila
        r = 0
    else:
        r = fila - col
        c = 0
    while c < 8 and r < 8:
        if tablero[r][c] == 'R':
            return False
        r =r+1
        c =c+1

    if fila <= col:
        r = 0
        c = col + fila
        if c > 7:
            r = c - 7
            c = 7
    else:
        c = 7
        r = fila - (7 - col)

    while c >= 0 and r < 8:
        if tablero[r][c] == 'R':
            return False
        r =r+1
        c =c-1

    return True

def agregar_reina(n):
    if n < 1:
        return True

    for x in range(8):
        for y in range(8):
            if celda_libre(x, y):
                tablero[x][y] = 'R'
                if agregar_reina(n-1):
                    return True
                else:
                    tablero[x][y] = '0'
    return False

tablero = []
for i in range(8):
    tablero.append(['0'] * 8)
agregar_reina(8)
for row in tablero:
    print(*row)