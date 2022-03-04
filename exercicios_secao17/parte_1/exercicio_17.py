"""
17) Escreva um código que apresente a classe Eletrdoméstico, com atributo
ligado e o método imprimir. O método imprimir deve mostrar na tela os valores de
todos os atributos. O atributo ligado será booleano e deverá indica o estado
atual do eletrodoméstico, se ligado ou desligado.
"""


class Eletrodomestico:
    def __init__(self, ligado):
        self.ligado = ligado

    def imprimir(self):
        if self.ligado:
            return print('\nO eletrodomestico está ligado')
        return print('\nO eletrodomestico está desligado')


eletro = Eletrodomestico(False)
eletro1 = Eletrodomestico(True)
eletro.imprimir()
eletro1.imprimir()
