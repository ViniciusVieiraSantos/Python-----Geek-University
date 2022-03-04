"""
14) Faça um programa que leia um vetor de 10 posições e verifique se existem
valores iguais e os escreva na tela.
"""
from random import randint

vetor = [randint(1, 20) for i in range(10)]
print(f'\nVetor : {vetor}')
numero_iguais = {numero for numero in vetor if vetor.count(numero) > 1}

print(f'Numeros iguais : {numero_iguais}')
