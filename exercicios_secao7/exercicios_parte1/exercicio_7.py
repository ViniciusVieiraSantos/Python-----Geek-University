"""
7) Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
Imprima o vetor, o maior elemento e a posição que ele se encontra.
"""
from random import randint
count_par = 0

vetor = [randint(1, 30) for i in range(10)]
print(f'Vetor lido :{vetor}\n')

print(f'O maior elemento é {max(vetor)} e esta na posição : {vetor.index(max(vetor))}')
