"""
4) Faça uma função para verificar se um número é um quadrado perfeito.
Um quadrado perfeito é um número inteiro não negativo que pode ser
expresso como o quadrado de outro número inteiro. Ex: 1, 4, 9...
"""


def quadrado_perfeito(num):
    if num > 0:
        raiz = int(num ** 0.5)
        if raiz ** 2 == num:
            return f'O numero {num} é um quadrado perfeito'
    return f'O numero {num} não é um quadrado perfeito'


x = int(input('Digite um numero: '))
print(quadrado_perfeito(x))
