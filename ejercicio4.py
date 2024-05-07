abc = [['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-']]


def fnt_agregar(dato, x, y):

    if dato == 'A' and (x == 0 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'B' and (x == 0 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'C' and (x == 0 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'D' and (x == 0 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'E' and (x == 0 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'F' and (x == 0 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'G' and (x == 1 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'H' and (x == 1 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'I' and (x == 1 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'J' and (x == 1 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'K' and (x == 1 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'L' and (x == 1 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'M' and (x == 2 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'N' and (x == 2 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'Ñ' and (x == 2 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'O' and (x == 2 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'P' and (x == 2 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'Q' and (x == 2 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'R' and (x == 3 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'S' and (x == 3 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'T' and (x == 3 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'U' and (x == 3 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'V' and (x == 3 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'W' and (x == 3 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'X' and (x == 4 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'Y' and (x == 4 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'Z' and (x == 4 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'CH' and (x == 4 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()  
    elif dato == 'LL' and (x == 4 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'RR' and (x == 4 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    else:
        input('\nEsta letra no va ahí <ENTER>')

def fnt_impresion_matriz():
    for i in range(len(abc)):
        for j in range(len(abc[i])):
            print(abc[i][j], end='  ')
        print()
         
sw = True
while sw == True:

    import os
    os.system('cls')
    fnt_impresion_matriz()
    fnt_agregar(input('Dato: '), int(input('Fila: ')), int(input('Columna: ')))
