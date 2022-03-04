"""
4) Baseando-se no exercício 3 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
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
