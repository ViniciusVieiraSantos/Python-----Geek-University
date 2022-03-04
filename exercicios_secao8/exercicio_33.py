"""
33) Faça uma função que receba um número N e retorne a soma dos algarismos de N!.
Ex: se N = 4, N! = 24. logo, a soma de seus algarismos é 2 + 4 = 6.
"""


def soma_n(numero):
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial *= i
    algarismos = str(fatorial)
    soma = 0

    for i in range(len(algarismos)):
        soma += int(algarismos[i])

    return soma


x = int(input('Digite um numero inteiro positivo: '))
if x < 0:
    while x < 0:
        x = int(input('Digite um numero inteiro positivo: '))
print(f'Soma dos algarismos : {soma_n(x)}')
