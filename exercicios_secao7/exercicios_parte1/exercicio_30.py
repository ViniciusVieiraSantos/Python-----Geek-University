"""
30)Faça um programa que leia dois vetores de 10 elementos. Crie
um vetor que seja a intersecção entre os 2 vetores anteriores, ou seja, que
contém apenas os números que estão em ambos os vetores. Não deve
conter números repetidos.
"""
from random import randint
vetor_1 = {randint(1, 20) for i in range(10)}
vetor_2 = {randint(1, 20) for b in range(10)}

vetor_3 = vetor_1.intersection(vetor_2)
print(f' conjunto 1: {vetor_1}\nconjunto 2: {vetor_2}\nintersecção dos 2 conjuntos:{vetor_3}')
