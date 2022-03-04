"""
65) Implemente a função a qual recebe duas strings, str1 e str2, e um
valor inteiro positivo N. A função concatena não mais que N caractere
da string apontada por str2 à string apontada por str1 e termina str1 com NULL.
"""


def concatenar_strings(frase_1, frase_2, numero):
    lista_1, lista_2 = list(frase_1), list(frase_2)
    for i in range(numero):
        lista_1.insert(i, lista_2[i])
    lista_1.append('')
    return lista_1


x = ' e Bonito'
y = 'O Brasil é muito grande'
z = int(input('Numero de caracteres a serem concatenados : '))
print(concatenar_strings(x, y, z))


