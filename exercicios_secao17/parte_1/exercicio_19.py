"""
19) Baseando-se no exercicio 18 adicione os métodos ligar e desligar
que deverão mudar o conteúdo do atributo ligado conforme o caso.
"""


class Eletrodomestico:
    def __init__(self):
        self.ligado = False

    def imprimir(self):
        if self.ligado:
            return print('O eletrodomestico está ligado.')
        print('O eletrodomestico está desligado.')

    def ligar(self):
        if self.ligado:
            return print('O eletrodomestico já está ligado.')
        self.ligado = True
        print('Ligando....')

    def desligar(self):
        if not self.ligado:
            return print('O eletrodomestico já está desligado.')
        self.ligado = False
        print('Desligando....')


print()
eletro = Eletrodomestico()
eletro.imprimir()
eletro.desligar()
eletro.imprimir()
eletro.ligar()
eletro.imprimir()
eletro.ligar()
eletro.desligar()
eletro.imprimir()
