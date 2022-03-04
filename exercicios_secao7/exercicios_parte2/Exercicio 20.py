"""
20) Faça um programa que leia uma matriz 3 x 6 com valores reais.
(a) Imprima a soma de todos os elementos das colunas ímpares.
(b) Imprima a média aritmética dos elementos da segunda e quarta colunas.
(c) Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
(d) Imprima a matriz modificada.
"""

from random import uniform


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


def soma_colunas_impares(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j % 2 != 0:
                soma += matriz[i][j]
    soma = round(soma, 1)
    return f'Soma colunas impares : {soma}'


def media_coluna2_4(matriz):
    media = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == 1 or j == 3:
                media += matriz[i][j]
    media /= 6
    media = round(media, 1)
    return f'Media da segunda e quarta coluna : {media}\n'


def substituir_6coluna(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == 5:
                soma = matriz_1[i][1] + matriz_1[i][2]
                matriz[i][j] = round(soma, 1)
                soma = 0
    return matriz


matriz_1 = [[round(uniform(0, 20), 1) for j in range(6)] for i in range(3)]

print('\nMatriz :')
imprimir_matriz(matriz_1)
print(soma_colunas_impares(matriz_1))
print(media_coluna2_4(matriz_1))
matriz_1 = (substituir_6coluna(matriz_1))
print('Matriz modificada:')
imprimir_matriz(matriz_1)
