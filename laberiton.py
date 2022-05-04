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
    if laberinto[i][j] == "s":
        print("\npasos para salir: ",len(camino))
        print("\nPasos:\n",pasos,"\n")
        print("\nCamino:\n",camino,"\n")
        DibujarLaberinto() 
    else:   
        if i > len(laberinto)-1:
            RecorrerLaberinto2(i-1,j, "izquierda")
        elif i < 0:
            RecorrerLaberinto2(i+1, j+1, "arriba")
        elif j > len(laberinto[i])-1:
            RecorrerLaberinto2(i+1, j-1, "abajo")
        elif j < 0:
            RecorrerLaberinto2(i-1, j+1, "arriba")
        else:
            if laberinto[i][j] == " ":
                pasos.append(direccion)      
                laberinto[i][j] = "·"
                #DibujarLaberinto()
                camino.append([i,j])
                RecorrerLaberinto2(i,j+1, "derecha")    
            elif (laberinto[i][j] == "x" or laberinto[i][j] == "·" or laberinto[i][j] == "-") and direccion == "derecha":
                RecorrerLaberinto2(i+1, j-1, "abajo")
            elif (laberinto[i][j] == "x" or laberinto[i][j] == "·" or laberinto[i][j] == "-") and direccion == "abajo":
                RecorrerLaberinto2(i-1, j-1, "izquierda")
            elif (laberinto[i][j] == "x" or laberinto[i][j] == "·" or laberinto[i][j] == "-") and direccion == "izquierda":
                RecorrerLaberinto2(i-1, j+1, "arriba")
            elif (laberinto[i][j] == "x" or laberinto[i][j] == "·" or laberinto[i][j] == "-") and direccion == "arriba":
                #print("Sin salida")
                PasoAnterior = camino[-1]
                laberinto[PasoAnterior[0]][PasoAnterior[1]] = "-"
                camino.pop(-1)
                pasos.pop(-1)
                PasoAnterior = camino[-1]
                RecorrerLaberinto2(PasoAnterior[0],PasoAnterior[1]+1,"derecha")
    
pasos = []       
camino = []
DibujarLaberinto()
RecorrerLaberinto2(0,1, "abajo")                                