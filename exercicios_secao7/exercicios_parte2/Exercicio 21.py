"""
21) Faça um programa que leia duas matrizes 2 x 2 com valores reais.
Ofereça ao usuário um menu de opções:
(a) somar as duas matrizes
(b) subtrair a primeira matriz da segunda
(c) adicionar uma constante às duas matrizes
(d) imprimir as matrizes
"""
from random import uniform


def soma_matrizes(matriz1, matriz2):
    matriz3 = [[round(matriz1[i][j] + matriz2[i][j], 1) for j in range(2)] for i in range(2)]
    return matriz3


def subtrair_matrizes(matriz1, matriz2):
    matriz3 = [[round(matriz1[i][j] - matriz2[i][j], 1) for j in range(2)] for i in range(2)]
    return matriz3


def add_constante(matriz1, matriz2):
    constante = float(input('Digite uma constante : '))
    for i in range(2):
        for j in range(2):
            matriz1[i][j], matriz2[i][j] = matriz1[i][j] + constante, matriz2[i][j] + constante
    return matriz1, matriz2


def imprimir_matriz(matriz):
    t = len(matriz)
    for c in range(t):
        print(end='| ')

        for d in range(len(matriz[c])):
            print(matriz[c][d], end=' ')     # imprimir o valor do elemento da matriz

        print(end='|\n')
    print()     # print para pular uma linha


matriz_1 = [[round(uniform(0, 30), 1)for j in range(2)] for i in range(2)]
matriz_2 = [[round(uniform(0, 30), 1)for n in range(2)] for m in range(2)]

x = -1
while x != 0:
    x = int(input('\nMenu:\n   1 - Somar as matrizes\n   2 - Subtrair as matrizes\n   3 - Adicionar uma constante as '
                  'duas matrizes''\n   4 - imprimir as duas matrizes\n   0 - Sair\nDigite um numero : '))
    if x == 0:
        break
    if x == 1:
        matriz_soma = soma_matrizes(matriz_1, matriz_2)
        print('\nSoma das matrizes: ')
        imprimir_matriz(matriz_soma)

    if x == 2:
        matriz_sub = subtrair_matrizes(matriz_1, matriz_2)
        print('\nSubtração das matrizes: ')
        imprimir_matriz(matriz_sub)

    if x == 3:
        matriz_1, matriz_2 = add_constante(matriz_1, matriz_2)
        print('Matriz 1:')
        imprimir_matriz(matriz_1)
        print('Matriz 2:')
        imprimir_matriz(matriz_2)

    if x == 4:
        print('Matriz 1:')
        imprimir_matriz(matriz_1)
        print('Matriz 2:')
        imprimir_matriz(matriz_2)
