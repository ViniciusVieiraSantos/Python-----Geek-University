"""
34) Faça uma função não-recursiva que receba um número inteiro positivo impar N e
retorne o fatorial duplo desse número. O fatorial duplo é definido como
o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N.
Assim, o fatorial duplo de 5 é: 5!! = 1 * 3 * 5 = 15
"""


def fatorial_duplo(numero):
    fatorial = 1
    for i in range(numero, 1, -2):
        fatorial *= i
    return fatorial


x = int(input('Digite um numero inteiro positivo: '))
if x < 0:
    while x < 0:
        x = int(input('Digite um numero inteiro positivo: '))
print(f'Fatorial duplo : {fatorial_duplo(x)}')

