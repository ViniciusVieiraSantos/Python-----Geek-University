"""
26) Escreva um código que apresente a classe Microondas, com atributo
ligado e o método imprimir. O método imprimir deve mostrar na tela os
valores de todos os atributos. O atributo ligado será boleano e verá indicar
o estado atual do microondas, se ligado ou desligado.
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
