"""
8) Crie um programa que lê 6 valores inteiros , em seguida, mostre
na tela os valores lidos na ordem inversa
"""
from random import randint

vetor = [randint(1, 30) for i in range(6)]
print(f'\nVetor lido :{vetor}\n')


vetor_inverso = [vetor[j] for j in range(5, -1, -1)]
print(f'Vetor inverso : {vetor_inverso}')
