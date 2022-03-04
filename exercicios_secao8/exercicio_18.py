"""
18) Faça uma função que receba por parâmero dois valores X e Z.
Calcule e retorne o resultado de X elevado a Z para o programa principal.
Atenção não utilize nenhuma função pronta de exponenciação.
"""


def expoente(numero_1, numero_2):

    return numero_1 ** numero_2


x = int(input('Digite um numero para ser a base da exponenciação: '))

z = int(input('Digite um numero para ser o expoente da exponenciação: '))


print(f'{x}^{z} = {expoente(x, z)}')
