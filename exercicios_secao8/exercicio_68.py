"""
68) Faça uma função que receba duas string e retorne a intercalação letra a letra
da primeira com a segunda string. A string intercalada deve ser retornada na primeira string
"""


def intercalar_strings(string_1, string_2):
    intercalacao = ''
    if len(string_1) <= len(string_2):
        for i in range(len(string_1)):
            intercalacao += string_1[i] + string_2[i]

    else:
        for i in range(len(string_2)):
            intercalacao += string_1[i] + string_2[i]
    return intercalacao


str_1 = 'amarelo'
str_2 = 'LARANJA'

str_1 = intercalar_strings(str_1, str_2)
print(f'\n{str_1}')
