"""
46) Crie um programa contendo as seguintes funcões que recebem um vetor V
números reais como parâmetros:
. Impressão normal do vetor.
. Impressão inversa.
. Função que retorna a média aritmética dos elementos do vetor.
"""
from random import randint


def normal_vetor(vetor):
    return f'Vetor normal : {vetor}'


def inverso_vetor(vetor):
    return f'Vetor normal :{vetor[::-1]}'


def media_vetor(vetor):
    return f'Media vetor : {sum(vetor)/len(vetor)}'


vet = []
n = int(input('Digite o tamanho do vetor a ser gerado: '))

for i in range(0, n):
    valor = randint(0, 100)
    while valor in vet:
        valor = randint(0, 100)
    vet.append(valor)

print(f'Vetor normal : {normal_vetor(vet)}\nVetor inverso : {inverso_vetor(vet)}\nMedia vetor : {media_vetor(vet)}')
