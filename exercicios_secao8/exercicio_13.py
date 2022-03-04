"""
13) Faça uma função que receba dois valores numéricos e um símbolo.
Este símbolo representará a operação que se deseja efetuar com os
números. Se o símbolo for + deverá ser realizada uma adição, se for -
uma subtração, se for / uma divisão e se for * será efetuada uma multiplicação.
"""


def soma_algarimos(numero_1, numero_2, simbolo):
    if simbolo == '+':
        return print(f'Soma : {numero_2 + numero_1}')
    elif simbolo == '-':
        return print(f'Subtração : {numero_2 - numero_1}')
    elif simbolo == '/':
        return print(f'Divisão : {numero_2 / numero_1}')
    elif simbolo == '*':
        return print(f'Multiplicação : {numero_2 * numero_1}')
    return print('\nSimbolo invalido')


a = int(input("Digite um numero inteiro maior que 0: "))
b = int(input("Digite um numero inteiro maior que 0: "))
c = str(input("Digite + para somar , - para subtrair , / para dividir , *para multiplicar : "))
soma_algarimos(a, b, c)
