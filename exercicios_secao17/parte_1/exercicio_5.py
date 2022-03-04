"""
5) Escreva um código que apresente a classe Retangulo, com atributos
comprimento, largura, área e perímetro e, os métodos calcularArea,
calcularPerimetro e imprimir. Os métodos calcularArea e calcularPerimetro
devem efetuar seus respectivos cálculos e colocar os valores nos atributos area
e perimetro. O método imprimir deve mostrar na tela os valores de todos os
atributos. Salienta-se que a área de retângulo é obtida peça fórmula (comprimento *
largura) e o perímetro por (2 * comprimento) + (2 * largura)
"""


class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        self.area = self.calcular_area()
        self.perimetro = self.calcular_perimetro()

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return (2 * self.comprimento) + (2 * self.largura)

    def imprimir(self):
        print(f'\nRetangulo:\nComprimento : {self.comprimento}  Largura: {self.largura}  Area : {self.area}  '
              f'Perimetro : {self.perimetro}')


ret = Retangulo(5, 8)
ret.imprimir()
