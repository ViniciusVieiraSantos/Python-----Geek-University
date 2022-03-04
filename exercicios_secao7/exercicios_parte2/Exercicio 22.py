"""
22) Faça um programa que leia duas matrizes A e B
de tamanho 3 x 3 e calcule C = A * B.
"""

from random import randint


def imprimir_matriz(matriz):
    t = len(matriz)
    for c in range(t):
        print(end='| ')

        for d in range(len(matriz[c])):
            if matriz[c][d] < 100:
                print(end=' ')              # imprimir espaço em branco para alinhar a matriz
                if matriz[c][d] < 10:
                    print(end=' ')          # imprimir espaço em branco para alinhar a matriz

            print(matriz[c][d], end=' ')     # imprimir o valor do elemento da matriz

        print(end='|\n')
    print()     # print para pular uma linha


def mult_matrizes(matriz1, matriz2):
    matriz3 = [[matriz1[i][j] * matriz2[i][j] for j in range(2)] for i in range(2)]
    return matriz3


matriz_1 = [[randint(0, 30) for j in range(2)] for i in range(2)]
matriz_2 = [[randint(0, 30) for n in range(2)] for m in range(2)]
matriz_3 = mult_matrizes(matriz_1, matriz_2)
print('Matriz 1 : ')
imprimir_matriz(matriz_1)
print('Matriz 2 : ')
imprimir_matriz(matriz_2)
print('Matriz 3 : ')
imprimir_matriz(matriz_3)
