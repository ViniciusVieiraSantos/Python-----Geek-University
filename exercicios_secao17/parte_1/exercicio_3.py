"""
3) Escreva um código que apresente a classe Quadrado, com atributos
lado, área e perímetro e, os métodos calcularArea, calcularPerimetro
e imprimir. Os métodos calcularArea e calcularPerimetro devem efetuar
seus respectivos cálculos e colocar os valores nos atributos area e
perimetro. O método imprimir deve mostrar na tela os valores de todos
os atributos. Salienta-se que a área de um quadrado é obtida pela
fórmula (lado * lado) e o perímetro por (4 * lado).
"""


class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        self.area = self.calcular_area()
        self.perimetro = self.calcular_perimetro()

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado

    def imprimir(self):
        print(f'\nQuadrado:\nLado: {self.lado}  Area:{self.area}  Perimetro: {self.perimetro}')


quadrado = Quadrado(5)
quadrado.imprimir()
