"""
62) Crie uma função que calcule o comprimento de uma string.
"""


def tamanho_string(string):
    tamanho = 0
    for _ in string:
        tamanho += 1
    return tamanho


x = str(input('Escreva uma palavra: '))

print(f'Tamanho da string: {tamanho_string(x)}')
