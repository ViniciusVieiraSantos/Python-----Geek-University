"""
23) Basenado-se no exercício 22 adicione os atributos numeroCanais
e, volumeMaximo, onde numeroCanais indica o número máximo de canais
que o televisor pode sintonizar e volumeMaximo indica qual o maior nível
de volume possível. O método imprimir deve ser modificado de forma a mostrar
na tela os valores de todos os atributos.
"""


class Televisor:
    def __init__(self):
        self.ligado = False
        self.canal = 1
        self.volume = 1
        self.n_canais = 20
        self.volume_max = 50

    def imprimir(self):
        print(f'\nLigado: {self.ligado}  Canal: {self.canal}  Volume: {self.volume}  Numero de Canais: {self.n_canais}'
              f'  Volume maximo: {self.volume_max}')

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
televisao.ligar()
televisao.imprimir()
televisao.desligar()
