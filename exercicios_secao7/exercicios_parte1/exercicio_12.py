"""
12) Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores
lidos juntamente com o maior, o menor e a média dos valores.
"""
from random import randint

vetor = [randint(1, 20) for i in range(5)]
print(f'\nVetor : {vetor}  \nMaior valor : {max(vetor)}  Menor Valor: {min(vetor)}   Media : {sum(vetor)/len(vetor)}')
