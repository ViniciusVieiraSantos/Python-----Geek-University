"""
63) Crie uma função que compara duas string e que retorna se elas
são iguais ou diferentes
"""


def verifica_igual(frase_1, frase_2):
    if frase_1 == frase_2:
        return 'As frases são iguais'
    return 'As frases não são iguais'


x = 'Frase igual'
y = 'Frase igual'
print(verifica_igual(x, y))
