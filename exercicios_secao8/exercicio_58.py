"""
58) Faça uma função que receba, por parâmetro, duas matrizes quadradas
de ordem N, A e B, e retorna uma matriz C que seja o produto matricial de A e B
"""

from random import randint


def mult_matrizes(matriz_a, matriz_b, n):
    mult = 0
    matriz_c = [[0 for j in range(n)] for i in range(n)]

    for x in range(n):
        for coluna_c in range(n):
            for y in range(n):
                mult += matriz_a[x][y] * matriz_b[y][coluna_c]
            matriz_c[x][coluna_c] = mult
            mult = 0
    return matriz_c


def imprimir_matriz(matriz):
    t = len(matriz)
    for c in range(t):
        print(end='| ')

        for d in range(t):
            if matriz[c][d] < 100:
                print(end=' ')  # imprimir espaço em branco para alinhar a matriz
                if matriz[c][d] < 10:
                    print(end=' ')  # imprimir espaço em branco para alinhar a matriz

            print(matriz[c][d], end=' ')  # imprimir o valor do elemento da matriz

        print(end='|\n')
    print()  # print para pular uma linha


ordem = int(input('Digite o tamanho das matrizes a serem geradas : '))


mat_a = [[randint(0, 10) for j in range(ordem)] for i in range(ordem)]
mat_b = [[randint(0, 10) for b in range(ordem)] for a in range(ordem)]

print('Matriz A:')
imprimir_matriz(mat_a)
print('Matriz B:')
imprimir_matriz(mat_b)
print('matriz C:')
m_c = mult_matrizes(mat_a, mat_b, ordem)
imprimir_matriz(m_c)
