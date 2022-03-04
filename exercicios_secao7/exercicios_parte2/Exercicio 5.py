"""
5) Leia uma matriz 5 x 5. Leia também um valor X. O programa
deverá fazer uma busca desse valor na matriz e, ao final, escrever a localização
(linha e coluna) ou mensagem de "não encontrado".
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


def procura_valor(valor, matriz):
    cont = 0

    for i in range(5):
        for j in range(5):
            if x == matriz[i][j]:
                print(f'O valor {valor} está na linha {i + 1} na coluna {j + 1} .')
                cont += 1
    if cont == 0:
        return print('Não encontrado.\n')


matriz_1 = [[randint(0, 30) for j in range(5)] for i in range(5)]      # Criar a matriz de forma aleatoria

imprimir_matriz(matriz_1)

x = int(input('Escreva um valor para saber se está na matriz: '))

procura_valor(x, matriz_1)
