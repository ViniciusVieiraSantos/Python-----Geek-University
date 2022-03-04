"""
52) Escreva uma função que recebe uma matriz quadrada de ordem
N e calcule a sua transposta (se B é a matriz transposta de A então aij = bji).
"""
from random import randint


def matriz_transposta(matriz):
    t = len(matriz)
    matriz_b = [[matriz[b][a] for b in range(t)] for a in range(t)]

    return matriz_b


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

print('Matriz A:')
imprimir_matriz(mat)
print('Matriz A transposta:')
imprimir_matriz(matriz_transposta(mat))
