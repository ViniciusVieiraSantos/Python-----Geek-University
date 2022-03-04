"""
12) Escreva uma função que receba um número inteiro maior que zero
e retorne a soma de todos os seus algarismos. Por exemplo,
ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido
não for maior do que zero, o programa terminará com a mensagem "Número inválido"
"""


def soma_algarimos(numero):
    if numero > 0:
        algarismos = str(numero)
        soma = 0

        for i in algarismos:
            soma += int(i)

        return print(f'Soma dos algarismos : {soma}')
    return print('Numero invalido')


a = int(input("Digite um numero inteiro maior que 0: "))
soma_algarimos(a)
