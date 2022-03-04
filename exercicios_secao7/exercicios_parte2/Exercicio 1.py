"""
1) Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
"""
from random import randint
matriz = [[randint(0, 12) for j in range(4)] for i in range(4)]
print(matriz)

contador = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            contador += 1
print(f'Valores maiores que 10 : {contador}')
