"""
7) Escreva um código que apresente a classe Circulo,
com atributos raio, área e perímetro e, os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calculaPerimetro
devem efetual seus respectivos cálculos e colocar os valores nos atributos
area e perimetro. O método imprimir deve mostrar na tela os valores de todos
os atributos. Salienta-se que a área de um círculo é obtida pela fórmula
(pi * raio * raio) e o perímetro por (2 * pi * raio), onde pi = 3,141516
"""


class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.area = self.calcular_area()
        self.perimetro = self.calcular_perimetro()

    def calcular_area(self):
        return 3.141516 * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * self.raio * 3.141516

    def imprimir(self):
        print(f'\nCirculo:\nComprimento : {self.raio}  Area : {self.area}  '
              f'Perimetro : {self.perimetro}')


c = Circulo(4)
c.imprimir()

