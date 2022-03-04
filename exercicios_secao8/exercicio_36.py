"""
36) Faça uma função não-recursiva que receba um número inteiro positivo N
e retorne o superfatorial desse número. O superfatorial e um número N
é deifinida pelo produto dos N primeiros fatoriais de N. Assim, o super
fatorial de 4 é sf(4) = 1! * 2! * 3! * 4! = 288
"""


def super_fatorial(numero):
    fatorial = 1
    for i in range(numero, 1, -1):
        for j in range(i, 1, -1):
            fatorial *= j
    return fatorial


x = int(input('Digite um numero inteiro positivo: '))
if x < 0:
    while x < 0:
        x = int(input('Digite um numero inteiro positivo: '))
print(f'Super fatorial: { super_fatorial(x)}')
