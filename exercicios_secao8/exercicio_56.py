"""
56) Faça uma função que recebe, por parâmetro, uma matriz A[7][6] e uma linha N
e retorne a soma dos elementos dessa linha.
"""
from random import randint


def soma_linha(matriz, linha):
    soma = 0
    for coluna in range(6):
        soma += matriz[linha][coluna]
    return soma


def imprimir_matriz(matriz):
    t = len(matriz)
    for c in range(t):
        print(end='| ')

        for d in range(6):
            if matriz[c][d] < 100:
                print(end=' ')              # imprimir espaço em branco para alinhar a matriz
                if matriz[c][d] < 10:
                    print(end=' ')          # imprimir espaço em branco para alinhar a matriz

            print(matriz[c][d], end=' ')     # imprimir o valor do elemento da matriz

        print(end='|\n')
    print()     # print para pular uma linha


mat = [[randint(0, 10) for j in range(6)] for i in range(7)]

x = int(input('Digite o numero da linha (1 a 7) da matriz A a ser somada: '))
if x < 1 or x > 7:
    while x < 1 or x > 7:
        print(f'A matriz não possui a linha {x}, digite um valor entre 1 e 7  : ')
        x = int(input())

print('Matriz A:')
imprimir_matriz(mat)
print(f'Soma dos elementos da linha {x} : {soma_linha(mat, x -1)}')
