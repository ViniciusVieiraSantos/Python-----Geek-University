"""
14) Faça um prorgrama para gerar automaticamente números entre 0 e 99 de uma
cartela de bingo. Sabendo que cada cartela deverá conter 5 linhas de 5
números, gere estes dados de modo a não ter números repetidos dentro das cartelas.
O programa deve exibir na tela a cartela gerada.
"""
from random import randint
numeros = []


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


def gerar_numeros():

    numero = randint(0, 99)
    while numero in numeros:
        numero = randint(0, 99)
    numeros.append(numero)
    return numero


matriz_1 = [[gerar_numeros() for j in range(5)] for i in range(5)]
print('Matriz :')
imprimir_matriz(matriz_1)
