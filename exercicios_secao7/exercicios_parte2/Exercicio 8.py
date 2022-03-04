"""
8) Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que
estão acima da diagonal principal.
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


def soma_acima_diagonal(matriz):
    soma = 0
    for i in range(3):
        for j in range(3):
            if j > i:
                soma += matriz_1[i][j]
    return soma


matriz_1 = [[randint(1, 40) for j in range(3)] for i in range(3)]
print('\nMatriz:')
imprimir_matriz(matriz_1)
print(f'Soma dos elementos acima da diagonal principal: {soma_acima_diagonal(matriz_1)}')