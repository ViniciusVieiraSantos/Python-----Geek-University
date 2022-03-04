"""
55) Faça uma função que recebe, por parâmetro, uma matriz A[3][3] e
retorna a soma dos elementos da sua diagonal principal e da sua diagonal secundária
"""
from random import randint


def soma_diagonais(matriz):
    soma_diagonal = 0
    soma_diagonal_secudaria = 0
    t = len(matriz)
    for a in range(t):
        for b in range(t):
            if a == b:
                soma_diagonal += matriz[a][b]
            if a + b == 2:
                soma_diagonal_secudaria += matriz[a][b]
    return soma_diagonal, soma_diagonal_secudaria


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


n = 3
mat = [[randint(0, 10) for j in range(n)] for i in range(n)]

print('Matriz A:')
imprimir_matriz(mat)
a, b = soma_diagonais(mat)
print(f'Soma dos elementos da diagonal principal : {a}')
print(f'Soma dos elementos da diagonal secundaria :{b}')

