"""
5) Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""

from random import randint
count_par = 0

vetor = [randint(1, 30) for i in range(10)]
print(f'Vetor lido :{vetor}\n')

for j in vetor:
    if j % 2 == 0:
        count_par += 1

print(f"O vetor possui {count_par} valores pares")
