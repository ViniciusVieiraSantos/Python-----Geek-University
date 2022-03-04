"""
2) Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0
os demais elementos. Escreva ao final matriz obtida
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


matriz_1 = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
print('\nMatriz :')
imprimir_matriz(matriz_1)
