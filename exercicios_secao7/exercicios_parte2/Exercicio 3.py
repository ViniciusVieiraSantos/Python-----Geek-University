"""
3) Faça um programa que preenche uma matriz 4 x 4 com o produto do valor da linha
e da coluna de cada elemento. Em seguida, imprima na tela a matriz.
"""


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


matriz_1 = [[i * j for j in range(4)] for i in range(4)]
print('\nMatriz: ')
imprimir_matriz(matriz_1)
