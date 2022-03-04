"""
61) Escreva uma função que compare e retorne verdadeiro, caso uma string
seja anagrama da outra, e falso, caso contrario.
"""


def verifica_anagrama(string_1, string_2):
    if len(string_1) != len(string_2):
        return 'As palavras não são um anagrama'

    lista_1, lista_2 = sorted(list(string_1)), sorted(list(string_2))
    if lista_1 == lista_2:
        return 'As palavras são anagrama da outra'

    return 'As palavras não são um anagrama'


x = str(input('Escreva uma palavra: '))
y = str(input('Escreva outra palavra: '))

print(verifica_anagrama(x, y))

