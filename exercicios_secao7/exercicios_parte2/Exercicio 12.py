"""
12) Leia uma matriz de 3 x 3 elementos. Calcule e imprima a sua transposta.
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


matriz_1 = [[randint(1, 30) for j in range(3)] for i in range(3)]
matriz_transposta = [[matriz_1[j][i] for j in range(3)] for i in range(3)]
print('\nMatriz :')
imprimir_matriz(matriz_1)
print('\nMatriz transposta:')
imprimir_matriz(matriz_transposta)