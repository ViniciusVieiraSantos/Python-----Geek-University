"""
20) Escreva um programa que leia números inteiros no intervalo [0,50]
e os armazene em um vetor com 10 posições. Preencha um segundo vetor
apenas com os números ímpares do primeiro vetor. Imprima os dois vetores,
2 elementos por linha.
"""
from random import randint

vetor = [randint(0, 50) for i in range(10)]
vetor_impar = [num for num in vetor if num % 2 != 0]

print("Vetor: ")
for i in range(0, 10, 2):
    print(vetor[i], vetor[i+1])
print()

print("Vetor impar: ")
x = 0
while x < len(vetor_impar):
    if x == len(vetor_impar) - 1:
        print(vetor_impar[-1])
        break
    print(vetor_impar[x], vetor_impar[x + 1])
    x += 2



