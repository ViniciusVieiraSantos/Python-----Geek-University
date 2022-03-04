"""
32) Faça uma funçao chamada 'simplifica' que recebe como parâmetro o numerador
e o denominador de uma fração. Esta função deve simplificar a fração
recebebida dividindo o numero e o denominador pelo maior fator possível.
Por exemplo, a fração 36/60 simplifica para 3/5 dividindo o numerador e o denominador
por 12. A funcão deve modificar as variáveis passadas como parâmetro.
"""


def simplifica(a, b):
    maior_denominador = 1
    for x in range(1, a + b):
        if a % x == 0 and b % x == 0:
            maior_denominador = x
    return print(f"{int(a / maior_denominador)} / {int(b / maior_denominador)}")


simplifica(a=int(input("Insira o valor do numerador da fração\n")),
           b=int(input("Insira o valor do denominador da fração\n")))
