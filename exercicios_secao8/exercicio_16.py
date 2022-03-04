"""
16) Faça uma função chamada DesenhaLinha. Ele deve desenhar uma linha
na tela usando vários símbolos de igual (Ex: ========). A função recebe
por parâmetro quantos sinais de igual serão mostrados
"""


def desenha_linha(numero):
    return '=' * numero


print(desenha_linha(int(input('Numero de sinais: '))))
