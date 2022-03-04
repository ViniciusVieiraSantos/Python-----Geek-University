"""
47) Faça uma função que receba ua matriz de 4 x 4 e retorne quantos valores
maiores do que 10 ela possui
"""
from random import randint


def conta_valores(vetor):
    cont = 0
    for a in range(0, 4):
        for b in range(0, 4):
            if vetor[a][b] > 10:
                cont += 1
    return cont


vet = [[randint(0, 50) for j in range(4)] for i in range(4)]

print(f'Matriz :{vet}')
print(f'Quantidade de valores maiores que 10 : {conta_valores(vet)}')

