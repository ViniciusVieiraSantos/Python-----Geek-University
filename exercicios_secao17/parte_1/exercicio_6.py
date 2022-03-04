"""
6) Baseando-se no exercício 5 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação
do objeto.
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
