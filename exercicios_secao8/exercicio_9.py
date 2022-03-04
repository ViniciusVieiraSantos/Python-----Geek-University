"""
9) Faça uma função que receba a altura e o raio de um cilindro circular e
retorne o volume do cilindro. O volume de um cilindro circular é calculado por meio
da seguinte fórmula: V = r * (raio ** 2) * altura, onde r = 3.141592
"""


def volume_cilindro(altura, raio):
    volume = round(3.141592 * raio ** 2 * altura, 2)
    return volume


a = float(input("Digite o valor da altura do cilindro: "))
b = float(input("Digite o valor do raio do cilindro: "))
v = volume_cilindro(a, b)
print(f' Volume do cilindro : {v}')
