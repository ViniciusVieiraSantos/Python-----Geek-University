"""
64) Implemente a função a qual recee duas strings, str1 e str2, e
concatena a string apontada por str2 à string apontada por str1
"""


def concatenar_strings(frase_1, frase_2):
    return frase_2 + frase_1


x = ' e Bonito'
y = 'O Brasil é muito grande'

print(concatenar_strings(x, y))
