"""
19) Faça uma função que retorne o maior fator primo de um número.
"""


def maior_fator_primo(n):
    if n == 1:
        return 1

    fp = 2  # Nota: fp = fator primo
    while n != 1:
        if n % fp == 0:
            n = n / fp

        else:
            fp += 1

    return fp


valor = int(input('Digite um número inteiro maior que 0: '))
print(f'O maior fator primo de {valor} é {maior_fator_primo(valor)}')
