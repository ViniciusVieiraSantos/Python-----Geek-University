"""
60) Escreva uma função que retorne a primeira posição de uma sub-string
dentro de uma string. Caso a sub-string não seja encontrada, a função
deve retornar -1.
"""


def posi_substring(stri, substr):
    if substr in stri:
        return stri.index(substring)
    return -1


string = 'Sinta o prazer de viver,Sinta a felicidade dentro de você,A esperança existe, busque, acrediteA força está ' \
         'dentro de você.'
substring = 'prazer'

posicao = posi_substring(string, substring)
if posicao == -1:
    print('A substring não se encontra na string')
else:
    print(f'A substring se inicia na posição {posicao} da string')
