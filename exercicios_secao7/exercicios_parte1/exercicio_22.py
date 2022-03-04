"""
22) Faça um programa que leia dois vetores de 10 posições e calcule
outro vetor contendo, nas posições pares os valores do primeiro
e nas posições impares os valores do segundo.
"""
from random import randint

vetor_1 = [randint(1, 80) for i in range(10)]
vetor_2 = [randint(1, 80) for j in range(10)]
print(f'\nVetor 1: {vetor_1}\nVetor 2: {vetor_2}')

vetor_3 = [vetor_1[i] if i % 2 == 0 else vetor_2[i] for i in range(10)]
print(f'Vetor 3: {vetor_3}')
