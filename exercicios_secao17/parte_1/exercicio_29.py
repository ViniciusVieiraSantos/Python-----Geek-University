"""
29) Baseando-se no exercício 28 adicione o atributo portaFechada que
deverá ser boleano e deverá indicar se a porta do microondas está
ou não fechada. O método imprimir deve ser modificado de forma a mostrar
na tela os valores de todos os métodos.
"""


class Microondas:
    def __init__(self, fechada=False):
        self.ligado = False
        self.fechada = fechada

    def imprimir(self):
        if self.ligado and self.fechada:
            print('A porta está fechada e o microondas está ligado.')
        elif not self.ligado and self.fechada:
            print('A porta está fechada e o microondas está desligado.')
        else:
            print('A porta está aberta e o microondas está desligado.')

    def ligar(self):
        if self.ligado:
            print('O microondas já está ligado.')
        elif not self.fechada:
            print('A porta está aberta.Feche a porta antes de tentar ligar o microondas.')
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
print()
micro.ligar()

print()
micro.imprimir()

micro = Microondas(True)
print()
micro.imprimir()

print()
micro.ligar()
micro.imprimir()

print()
micro.desligar()
micro.imprimir()
