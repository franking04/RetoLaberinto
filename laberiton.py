from array import array

#laberinto_1
'''
laberinto = [
    [' ','x','x','x','x'],
    [' ','x',' ',' ',' '],
    [' ','x',' ','x',' '],
    [' ',' ',' ','x',' '],
    ['x','x','x','x','s']
    ]
'''

#laberinto 2
'''
laberinto = [
    ['x',' ','x','x','x','x'],
    ['x',' ',' ',' ',' ','x'],
    ['x',' ','x','x','x','x'],
    ['x',' ',' ',' ',' ','x'],
    ['x','x','x','x','s','x']
    ]
'''

#laberinto 3
'''
laberinto = [
    ['x',' ','x','x','x','x','x','x','x'],
    ['x',' ',' ','x',' ',' ',' ',' ','x'],
    ['x','x',' ','x',' ','x','x',' ','x'],
    ['x',' ',' ','x',' ','x','x',' ','x'],
    ['x',' ','x','x',' ',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ','x','x',' ','x'],
    ['x','x','x','x','x','x','x',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ','x','x',' ','x','x','x','x'],
    ['x',' ',' ','x',' ',' ',' ',' ','x'],
    ['x','x','s','x','x','x','x','x','x']
]
'''

#laberinto 4
'''
laberinto = [
    ['x',' ','x','x','x','x','x','x','x'],
    ['x',' ',' ','x',' ',' ',' ',' ','x'],
    ['x','x',' ','x',' ','x','x',' ','x'],
    ['x',' ',' ','x',' ','x','x',' ','x'],
    ['x',' ','x','x',' ','x','x',' ','x'],
    ['x',' ',' ',' ',' ','x','x',' ','x'],
    ['x','x','x','x','x','x','x',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ','x','x','x','x','x','x','x'],
    ['x',' ',' ',' ',' ','x','x','x','x'],
    ['x','x','x','x','s','x','x','x','x']
]
'''

#laberinto 5
'''
laberinto = [
    ['x',' ','x','x','x','x','x','x','x','x','x'],
    ['x',' ','x',' ',' ',' ',' ',' ',' ',' ','x'],
    [' ',' ','x',' ','x','x','x','x','x','x','x'],
    [' ','x','x',' ','x',' ',' ',' ',' ',' ','x'],
    [' ','x',' ',' ','x',' ','x','x','x',' ','x'],
    [' ','x',' ','x','x',' ','x',' ',' ',' ','x'],
    [' ',' ',' ','x',' ',' ','x',' ','x','x','x'],
    [' ','x','x','x',' ','x',' ',' ','x',' ','x'],
    [' ','x',' ',' ',' ','x',' ','x',' ',' ','x'],
    [' ','x',' ','x','x',' ',' ','x',' ','x','x'],
    [' ','x',' ','x',' ',' ','x',' ',' ','x','x'],
    [' ',' ',' ','x',' ','x',' ',' ','x',' ','s'],
    ['x','x','x','x',' ','x',' ','x','x',' ','x'],
    ['x',' ',' ',' ',' ','x',' ','x','x',' ','x'],
    ['x',' ','x',' ','x','x',' ','x','x',' ','x'],
    ['x',' ','x',' ','x',' ',' ','x','x',' ','x'],
    ['x',' ','x',' ','x','x',' ','x','x',' ','x'],
    ['x',' ','x',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x','x','x','x','x','x','x','x','x','x','x']
]
'''

#laberinto 6

laberinto = [
    ['x',' ','x','x','x','x','x','x','x','x','x'],
    ['x',' ','x',' ',' ',' ',' ',' ',' ',' ','x'],
    [' ',' ','x',' ','x','x','x','x','x','x','x'],
    [' ','x','x',' ','x',' ',' ',' ',' ',' ','x'],
    [' ','x',' ',' ','x',' ','x','x','x','x','x'],
    [' ','x',' ','x','x',' ','x',' ',' ',' ','x'],
    [' ',' ',' ','x',' ',' ','x',' ','x','x','x'],
    [' ','x','x','x',' ','x',' ',' ','x',' ','x'],
    [' ',' ',' ',' ',' ','x',' ','x',' ',' ','x'],
    [' ','x',' ','x','x',' ',' ','x',' ','x','x'],
    ['x','x',' ','x',' ',' ','x',' ',' ','x','x'],
    ['x',' ',' ','x',' ','x',' ',' ','x',' ','s'],
    [' ',' ','x','x',' ','x',' ','x','x',' ','x'],
    [' ','x','x',' ',' ','x',' ','x','x',' ','x'],
    [' ',' ',' ',' ','x','x',' ','x','x',' ','x'],
    [' ','x','x',' ','x',' ',' ','x','x',' ','x'],
    [' ','x','x','x','x','x',' ','x','x',' ','x'],
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x','x','x','x','x','x','x','x','x','x','x']
]


def DibujarLaberinto():
    print('\n')
    for i in range(len(laberinto)):
        print('|',end='')
        for j in range(len(laberinto[i])):
            if j+1 == len(laberinto[i]):
                print(laberinto[i][j],end='')
            else:
                print(laberinto[i][j],end=' ')
        print('|')

def RecorrerLaberinto2(i,j,direccion):
    PasoAnterior = []
    if i > len(laberinto)-1:
        RecorrerLaberinto2(i-1,j, "←")
    elif i < 0:
        RecorrerLaberinto2(i+1, j+1, "↑")
    elif j > len(laberinto[i])-1:
        RecorrerLaberinto2(i+1, j-1, "↓")
    elif j < 0:
        RecorrerLaberinto2(i-1, j+1, "↑")
    else:
        if laberinto[i][j] == "s":
            pasos.append(direccion)
            PasoAnterior = camino[-1]
            laberinto[PasoAnterior[0]][PasoAnterior[1]] = pasos[-1]
            camino.append([i,j])
            print("\npasos para salir: ",len(camino))
            print("\nPasos:\n",pasos,"\n")
            print("\nCamino:\n",camino,"\n")
            DibujarLaberinto()
        elif laberinto[i][j] == " ":
            if len(camino) == 0:
                laberinto[i][j] = direccion
            else:
                pasos.append(direccion)
                PasoAnterior = camino[-1]
                laberinto[PasoAnterior[0]][PasoAnterior[1]] = pasos[-1]
            #DibujarLaberinto()
            camino.append([i,j])
            RecorrerLaberinto2(i,j+1, "→")    
        elif (laberinto[i][j] == "x" or laberinto[i][j] == "-" or laberinto[i][j] == "→" or laberinto[i][j] == "↓" or laberinto[i][j] == "←" or laberinto[i][j] == "↑") and direccion == "→":
            RecorrerLaberinto2(i+1, j-1, "↓")
        elif (laberinto[i][j] == "x" or laberinto[i][j] == "-" or laberinto[i][j] == "→" or laberinto[i][j] == "↓" or laberinto[i][j] == "←" or laberinto[i][j] == "↑") and direccion == "↓":
            RecorrerLaberinto2(i-1, j-1, "←")
        elif (laberinto[i][j] == "x" or laberinto[i][j] == "-" or laberinto[i][j] == "→" or laberinto[i][j] == "↓" or laberinto[i][j] == "←" or laberinto[i][j] == "↑") and direccion == "←":
            RecorrerLaberinto2(i-1, j+1, "↑")
        elif (laberinto[i][j] == "x" or laberinto[i][j] == "-" or laberinto[i][j] == "→" or laberinto[i][j] == "↓" or laberinto[i][j] == "←" or laberinto[i][j] == "↑") and direccion == "↑":
            #print("Sin salida")
            PasoAnterior = camino[-1]
            laberinto[PasoAnterior[0]][PasoAnterior[1]] = "-"
            camino.pop(-1)
            pasos.pop(-1)
            PasoAnterior = camino[-1]
            RecorrerLaberinto2(PasoAnterior[0],PasoAnterior[1]+1,"→")
    
pasos = []       
camino = []
DibujarLaberinto()
RecorrerLaberinto2(0,1, " ")                                