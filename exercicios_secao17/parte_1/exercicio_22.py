"""
22) Baseando-se no exercicio 21 adicione os métodos ligar e desligar
que deverão mudar o conteúdo do atributo ligado conforme o caso
"""


class Televisor:
    def __init__(self):
        self.ligado = False
        self.canal = 1
        self.volume = 1

    def imprimir(self):
        print(f'\nLigado: {self.ligado}  Canal: {self.canal}  Volume: {self.volume}')

    def ligar(self):
        if self.ligado:
            return print('A TV já esta ligada.')
        self.ligado = True
        return print('Ligando a TV .....')

    def desligar(self):
        if not self.ligado:
            return print('A TV já esta desligada.')
        self.ligado = False
        return print('Desligando a TV .....')


televisao = Televisor()
televisao.imprimir()
televisao.desligar()
televisao.ligar()
televisao.imprimir()
televisao.desligar()
