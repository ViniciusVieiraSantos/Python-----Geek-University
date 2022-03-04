"""
6) Faça um programa que receba do usuáro um vetor com 10 posições.
Em sequida deverá ser impresso o maior e o menor elemento do vetor.
"""
from random import randint
count_par = 0

vetor = [randint(1, 30) for i in range(10)]
print(f'Vetor lido :{vetor}\n')

print(f'O valor maximo é {max(vetor)}'f'\nO valor minimo é {min(vetor)}')
