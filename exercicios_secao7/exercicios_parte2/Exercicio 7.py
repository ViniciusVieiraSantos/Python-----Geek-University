"""
7) Gerar e imprimir uma matriz de tamanho de 10 x 10, onde
seus elementos são da forma:
A[i][j] = 2i + 7j - 2 se i < j:
A[i][j] = 3i² - 1 se i = j:
A[i][j] = 4i³ - 5j² + 1 se i > j:
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


def elemento_matriz(i, j):
    if i < j:
        return 2*i + 7*j - 2
    elif i == j:
        return 3*i - 1
    return 4*i**3 - 5*j**2 + 1


matriz_1 = [[elemento_matriz(i, j)for j in range(10)]for i in range(10)]
print('Matriz: ')
imprimir_matriz(matriz_1)
