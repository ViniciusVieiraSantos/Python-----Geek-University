"""
18) Faça um programa que leia um vetor de 10 números. Leia um
número x. Conte os múltiplos de um número inteiro x num vetor
e mostre-os na tela.
"""
from random import randint

vetor = [randint(1, 50) for i in range(10)]
print(f'\nVetor : {vetor}')

x = int(input('Digite um numero inteiro para descobrir quantos multiplos ele possui no vetor : '))
multiplos = {numero for numero in vetor if numero % x == 0}    # Criar como set para não repetir os numeros multiplos

print(f'Quantidade de multiplos de {x} : {len(multiplos)}\nNumeros multiplos : {multiplos}')

