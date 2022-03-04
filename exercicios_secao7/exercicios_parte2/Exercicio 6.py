"""
6) Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores
valores de cada posição das matrizes lidas.
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


matriz_1 = [[randint(0, 30) for j in range(4)] for i in range(4)]
matriz_2 = [[randint(0, 30) for n in range(4)] for m in range(4)]

print(f'Matriz 1 :')
imprimir_matriz(matriz_1)
print(f'Matriz 2 :')
imprimir_matriz(matriz_2)

matriz_3 = [[max(matriz_1[i][j], matriz_2[i][j]) for j in range(4)] for i in range(4)]
print(f'Matriz 3 :')
imprimir_matriz(matriz_3)
