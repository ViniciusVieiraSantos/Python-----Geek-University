"""
29) Faça um programa que receba 6 números inteiros e mostre:
    . Os números pares digitados;
    . A soma dos números pares digitados;
    . Os números ímpares digitados;
    . A quantidade de número ímpares digitados;
"""
from random import randint

vetor_1 = []   # vetor para numeros pares
vetor_2 = []   # vetor para numeros impares

vetor = [randint(1, 100) for i in range(6)]
print(f'\nVetor : {vetor}\n')

vetor = [vetor_1.append(numero) if numero % 2 == 0 else vetor_2.append(numero) for numero in vetor ]

print(f'Numeros pares digitados: {vetor_1}     Soma dos numeros pares: {sum(vetor_1)}\n')
print(f'Numeros impares digitados: {vetor_2}   Quantida de numeros impares:{len(vetor_2)}\n')

