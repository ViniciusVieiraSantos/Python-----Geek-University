"""
5) Faça uma função e um programa de teste para o cálculo do volume
de uma esfera. Sendo que o raio é passado por parâmetro.
V = 4/3 * r * R³
"""


def volume_esfera(raio):
    return round(4/3 * 3.14 * raio ** 3, 2)


volume = volume_esfera(int(input('Informe o raio da esfera: ')))
print(f'Volume da esfera é {volume}')
