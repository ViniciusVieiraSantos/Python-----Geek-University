"""
31) Faça um programa que leia dois vetores de 10 elementos. Crie
um vetor que seja a união entre os 2 vetores anteriores, ou seja,
que contém os números dos dois vetores. Não deve conter números
repetidos.
"""

from random import randint
vetor_1 = {randint(1, 20) for i in range(10)}
vetor_2 = {randint(1, 20) for b in range(10)}

print(f'Vetor 1 : {vetor_1}\nVetor 2 : {vetor_2}')
vetor_3 = vetor_1.union(vetor_2)
print(f'Vetor união : {vetor_3}')
