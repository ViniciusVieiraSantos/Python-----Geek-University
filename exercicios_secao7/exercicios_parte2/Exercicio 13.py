"""
13) Gere matriz 4 x 4 com valores no intervalo [1, 20]. Escreva um programa que transforme
a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os
elementos acima da diagonal principal. Imprima a matriz original e a matriz transformada.
"""

from random import randint


def imprimir_matriz(matriz):
    t = len(matriz)
    for c in range(t):
        print(end='| ')

        for d in range(t):
            if matriz[c][d] < 100:
                print(end=' ')              # imprimir espaço em branco para alinhar a matriz
                if matriz[c][d] < 10:
                    print(end=' ')          # imprimir espaço em branco para alinhar a matriz

            print(matriz[c][d], end=' ')     # imprimir o valor do elemento da matriz

        print(end='|\n')
    print()     # print para pular uma linha


def transforma_matriz_triangular(matriz):
    for i in range(4):
        for j in range(4):
            if j > i:
                matriz[i][j] = 0
    return matriz


matriz_1 = [[randint(1, 20) for j in range(4)] for i in range(4)]
print('\nMatriz : ')
imprimir_matriz(matriz_1)
matriz_1 = transforma_matriz_triangular(matriz_1)
print('\nMatriz transformada: ')
imprimir_matriz(matriz_1)
