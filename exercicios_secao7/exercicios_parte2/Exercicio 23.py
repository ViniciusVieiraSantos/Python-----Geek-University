"""
23) Faça um programa que leia uma matriz A de tamanho 3 x 3 e calcule B = A²
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


matriz_1 = [[randint(0, 30) for j in range(2)] for i in range(2)]
matriz_2 = [[matriz_1[m][n] ** 2 for n in range(2)] for m in range(2)]

print('Matriz  A: ')
imprimir_matriz(matriz_1)
print('Matriz B : ')
imprimir_matriz(matriz_2)
