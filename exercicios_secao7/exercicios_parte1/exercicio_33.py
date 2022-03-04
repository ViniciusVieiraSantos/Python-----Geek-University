"""
33) Faça um programa que leia um vetor de 15 posições e o compacte, ou
seja, elimine as posições com valor zero. Para isso, todos os elementos
à frente do valor zero, devem ser movidos uma posição para trás no vetor.
"""

vetor = [1, 0, 3, 4, 5, 0, 3, 3, 0, 3, 4, 5, 0, 3, 0]
compactado = [n for n in vetor if n != 0]

print(f'Vetor : {vetor}\nVetor compactado : {compactado}')
