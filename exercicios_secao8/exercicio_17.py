"""
17) Faça ua função que receba dois números inteiros positivos
por parâmetro e retorne a soma dos N números inteiros existentes
entre eles.
"""


def soma_n(numero_1, numero_2):
    soma = 0
    for i in range(min(numero_1, numero_2), max(numero_1, numero_2)):
        soma += i
    return soma


a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))

print(f'Soma dos numeros inteiros entre {a} e {b} : {soma_n(a, b)}')
