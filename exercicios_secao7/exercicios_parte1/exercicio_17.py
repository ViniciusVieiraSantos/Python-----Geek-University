"""
17) Leia um vetor de 10 posições e atribua valor 0
para todos os elemntos que possírem valores negativos.
"""
from random import randint

vetor = [randint(-10, 20) for i in range(10)]
print(f'Vetor: {vetor}')
vetor = [numero if numero > 0 else 0 for numero in vetor]
print(f'\nVetor positivo: {vetor}')


