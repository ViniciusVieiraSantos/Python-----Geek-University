"""
44) Faça uma função que receba como parâmetro um vetor X de
30 elementos inteiros e retorne, também por parâmetro, dois vetores
A e B. O vetor A deve conter os elementos pares de X e o vetor B, os
elementos impares
"""

from random import randint


def gera_vetor(lista_1):
    a = []
    b = []
    [a.append(numero) if numero % 2 == 0 else b.append(numero)for numero in lista_1]
    return a, b


lista = []
for i in range(0, 30):
    valor = randint(0, 100)
    while valor in lista:
        valor = randint(0, 100)
    lista.append(valor)

print(f'Vetor gerado : {lista}')

vetor_par, vetor_impar = gera_vetor(lista)
print(f'Vetor A com valores pares: {vetor_par}\nVetor B com valores impares: {vetor_impar}')

