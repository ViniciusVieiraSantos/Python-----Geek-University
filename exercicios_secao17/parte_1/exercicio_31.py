"""
31) Basenado-se no exerício 30 modifique o método ligar para que só ligue
o equipamento quando a porta do mesmo estiver fechada, simulando assim
o funcionamento de um microondas.
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

    def fechar_porta(self):
        if self.fechada:
            print('A porta já está fechada')
        else:
            self.fechada = True
            print('A porta foi fechada.')

    def abrir_porta(self):
        if self.fechada:
            self.fechada = False
            self.ligado = False
            print('A porta foi aberta.')
        else:
            print('A porta já está aberta')


micro = Microondas()
print()
micro.ligar()

print()
micro.imprimir()

micro.fechar_porta()
print()
micro.imprimir()

print()
micro.ligar()
micro.imprimir()

