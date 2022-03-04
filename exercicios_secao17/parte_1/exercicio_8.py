"""
8) Baseando-se no exercício 7 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
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

