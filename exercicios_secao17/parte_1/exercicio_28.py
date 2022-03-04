"""
28) Baseando-se no exercício 27 adicione os métodos ligar e desligar
que deverão mudar o conteúdo do atributo ligado conforme o caso.
"""


class Microondas:
    def __init__(self):
        self.ligado = False

    def imprimir(self):
        if self.ligado:
            print('O microondas está ligado.')
        else:
            print('O microondas está desligado.')

    def ligar(self):
        if self.ligado:
            print('O microondas já está ligado.')
        else:
            self.ligado = True
            print('O microondas foi ligado.')

    def desligar(self):
        if not self.ligado:
            print('O microondas já está desligado.')
        else:
            self.ligado = False
            print('O microondas foi desligado.')


micro = Microondas()
micro.imprimir()
micro.desligar()
micro.ligar()
micro.ligar()
micro.desligar()
