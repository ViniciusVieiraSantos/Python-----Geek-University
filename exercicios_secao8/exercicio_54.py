"""
54) Faça uma função que recebe, por parâmetro, uma matriz A[4][4] e retorna
a soma dos seus elementos
"""

from random import randint


def soma_elementos(matriz):
    soma = 0
    t = len(matriz)
    for a in range(t):
        for b in range(t):
            soma += matriz[a][b]
    return soma


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


n = 4

mat = [[randint(0, 10) for j in range(n)] for i in range(n)]

print('Matriz A:')
imprimir_matriz(mat)
print(f'Soma dos elementos da matriz : {soma_elementos(mat)}')
