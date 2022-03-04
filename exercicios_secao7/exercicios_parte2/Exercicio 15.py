"""
15) Leia uma matriz 5 x 10 que se refere respostas de 10 quetões de
múltipla escolha, referentes a 5 alunos. Leia também um vetor de
10 posições contendo o gabarito de respostas que podem ser a, b, c ou d.
Seu programa deverá comparar as respostas de cada candidato com o gabarito
e emitir um vetor denominado resultado, contendo a pontuação correspondente a cada
aluno.
"""
from random import choice
numeros = []


def imprimir_respostas(matriz):

    for c in range(5):
        print(f'Aluno {c + 1}:', end=' ')
        print(str(matriz[c]).replace('[', '').replace(']', '').replace("'", ''))


def comparar_respostas(respostas):
    gabarito = ['b', 'b', 'c', 'a', 'd', 'a', 'a', 'c', 'd', 'd']
    resultado = []

    for i in range(5):
        acerto = 0

        for j in range(10):
            x = respostas[i][j]
            if x == gabarito[j]:
                acerto += 1
        resultado.append(acerto)
    return resultado


escolhas = ['a', 'b', 'c', 'd']
matriz_1 = [[choice(escolhas) for j in range(10)] for i in range(5)]
print('Respostas alunos:')
imprimir_respostas(matriz_1)
print(f'\nVetor resultado: {comparar_respostas(matriz_1)}')
