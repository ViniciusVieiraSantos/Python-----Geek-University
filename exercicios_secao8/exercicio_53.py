"""
53) Faça uma função que verifica se uma matriz quadrada de ordem
N é a matriz identidade.
"""
from random import randint


def verifica_matriz_identidade(matriz):

    t = len(matriz)
    for a in range(t):
        for b in range(t):
            if a == b and matriz[a][b] != 1:
                return 'não é uma matriz identidade'
            if a != b and matriz[a][b] != 0:
                return 'não é uma matriz identidade'
    return "é uma matriz identidade"


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


n = int(input('Digite o tamanho da matriz quadrada a ser gerada: '))

mat = [[randint(0, 999) for j in range(n)] for i in range(n)]

matriz_b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]        # Matriz identidade 3x3
matriz_c = [[1, 0, 30], [0, 1, 0], [0, 0, 1]]       # Matriz 3x3

print('Matriz A: ')
imprimir_matriz(mat)
print(f'A Matriz A {verifica_matriz_identidade(mat)}')
print(f'A matriz B {verifica_matriz_identidade(matriz_b)}')
print(f'A matriz C {verifica_matriz_identidade(matriz_c)}')
