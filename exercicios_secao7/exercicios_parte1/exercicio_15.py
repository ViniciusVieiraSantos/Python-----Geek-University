"""
15) Leia um vetor com 20 números inteiros. Escreva os elementos do vetor
eliminando elementos repetidos.
"""
from random import randint

vetor = [randint(1, 20) for i in range(20)]
print(f'\nVetor : {vetor}')

vetor = set(vetor)
print(f'Vetor sem repetição : {vetor}')
