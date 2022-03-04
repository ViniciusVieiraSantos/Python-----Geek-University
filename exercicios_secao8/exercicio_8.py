"""
8) Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = ((a ** 2) + (b ** 2)) ** 0.5. Faça uma função
que receba os valores de a e b e calcule o valor da hipotenusa através da equação
"""


def calc_hipotenusa(cateto_a, cateto_b):
    hipotenusa = round((cateto_a ** 2 + cateto_b ** 2) ** 0.5, 2)
    return print(f' Valor da hipotenusa {hipotenusa}')


a = float(input("Digite o valor do cateto A: "))
b = float(input("Digite o valor do cateto B: "))
calc_hipotenusa(a, b)
