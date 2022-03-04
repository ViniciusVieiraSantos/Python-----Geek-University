"""
4) Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e coluna)
do maior valor.
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

linha_m = matriz_1.index(max(matriz_1))
coluna_m = matriz_1[linha_m].index(max(matriz_1[linha_m]))

print('\nMatriz :')
imprimir_matriz(matriz_1)
print(f'Maior valor : linha {linha_m+1}  coluna {coluna_m+1}')  # considerando a primeira linha/coluna = 1
