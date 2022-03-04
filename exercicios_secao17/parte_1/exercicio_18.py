"""
18) Baseando-se no exercício 17 adicione um método construtor que permita
a definição de todos os atributos no momento da instanciação do objeto.
"""


class Eletrodomestico:
    def __init__(self, ligado):
        self.ligado = ligado

    def imprimir(self):
        if self.ligado:
            return print('\nO eletrodomestico está ligado')
        print('\nO eletrodomestico está desligado')


eletro = Eletrodomestico(False)
eletro1 = Eletrodomestico(True)
eletro.imprimir()
eletro1.imprimir()
