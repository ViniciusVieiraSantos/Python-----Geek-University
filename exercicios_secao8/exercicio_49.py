"""
49) Faça uma função que receba uma matriz de 3 x 3 elementos. Calcule
e retorne a soma dos elementos que estão abaixo da diagonal
"""
from random import randint


def conta_valores(vetor):
    soma = 0
    for a in range(3):
        for b in range(3):
            if a > b:
                soma += vetor[a][b]
    return soma


vet = [[randint(0, 50) for j in range(3)] for i in range(3)]

print(f'Matriz :{vet}')
print(f'Soma dos elementos acima da diagonal : {conta_valores(vet)}')

