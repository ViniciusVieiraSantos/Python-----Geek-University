"""
4) Faça um programa que leia um vetor de 8 posições e, em seguida,
leia também dois valores X e Y quaisquer correspondentes a duas posições
no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados
nas respectivas posições X e Y.
"""
from random import randint, sample

vetor = [randint(1, 10) for i in range(8)]
print(f'Vetor lido :{vetor}\n')
x, y = sample(vetor, 2)
print(f'Valor posição {vetor.index(x)} : {x}    Valor posição {vetor.index(y)} : {y}'
      f'\nSoma : {x+y}')
