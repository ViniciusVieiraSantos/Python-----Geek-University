"""
11) Faça um programa que preencha um vetor com 10 números reais,
calcule e mostre a quantidade de números negativos e a soma dos números
positivos desse vetor.
"""
from random import randint
cont_pos = 0
cont_neg = 0

vetor = [randint(-5, 10) for i in range(10)]
print(f'\nVetor : {vetor}')

for i in vetor:
    if i > 0:
        cont_pos += 1
    else:
        cont_neg += 1

print(f'\nNumeros negativos : {cont_neg}   Numeros positivos : {cont_pos}')
