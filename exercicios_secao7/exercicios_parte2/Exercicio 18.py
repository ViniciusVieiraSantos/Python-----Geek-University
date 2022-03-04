"""
18) Faça um programa que permita ao usuário entrar com uma matriz de
3 x 3 números inteiros. Em seguida, gere um array unidemensional
pela soma dos números de cada coluna da matriz e mostrar na tela
esse array. Por exemplo, a matriz:
    5   -8    10
    1    2   15
    25  10   7
Vai gerar um vetor, onde cada posição é a soma das colunas da matriz. A primeira
posição será 5 + 1 + 25, e assim por diante:
   31  4  32
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


def criar_vetor(matriz):
    vetor = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            vetor[j] += matriz_1[i][j]
    return vetor


print('\nMatriz: ')
matriz_1 = [[randint(0, 30) for j in range(3)] for i in range(3)]
imprimir_matriz(matriz_1)
print(f'Vetor: {criar_vetor(matriz_1)}')
