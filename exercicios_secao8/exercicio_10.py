"""
10) Faça uma função que receba dois números e retorne qual deles é o maior.
"""


def maior_numero(numero_1, numero_2):

    return print(f' O maior numero é {max([numero_1,numero_2])}')


a = int(input("Digite um numero inteiro: "))
b = int(input("Digite outro numero inteiro: "))
maior_numero(a, b)
