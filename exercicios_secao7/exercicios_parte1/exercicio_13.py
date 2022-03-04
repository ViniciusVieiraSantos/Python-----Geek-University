"""
13) Fazer um programa ler 5 valores e, em seguida, mostrar a posição onde
se encotram o maior e o menor valor.
"""
from random import randint

vetor = [randint(1, 20) for i in range(5)]
print(f'\nVetor : {vetor}  \nPosição maior valor : {vetor.index(max(vetor))} '
      f' Posição Menor Valor: {vetor.index(min(vetor))} ')
