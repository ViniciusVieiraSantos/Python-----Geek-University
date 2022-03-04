"""
27) Basenado-se no exercício 26 adicione um método construtor
que permita o definição de todos os atributos no momento da
instanciação do objeto.
"""


class Microondas:
    def __init__(self, ligado):
        self.ligado = ligado

    def imprimir(self):
        if self.ligado:
            print('O microondas está ligado.')
        else:
            print('O microondas está desligado.')


micro = Microondas(True)
micro.imprimir()
micro = Microondas(False)
micro.imprimir()
