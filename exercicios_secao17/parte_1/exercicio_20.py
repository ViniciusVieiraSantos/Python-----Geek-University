"""
20) Escreva um código que apresente a classe Televisor, com atributos
ligado, canal e volume e, o método imprimir. O método imprimir deve
mostrar na tela os valores de todos os atributos. O atributo ligado
será boleano e deverá indicar o estado atual do televisor, se ligado
ou desligado. O atributo canal deverá indicar o canal atual em que
o televisor está sintonizado. O atributo volume deverá indicar o volume
atual do televisor.
"""


class Televisor:
    def __init__(self, ligado=False, canal=1, volume=1):
        self.ligado = ligado
        self.canal = canal
        self.volume = volume

    def imprimir(self):
        print(f'\nLigado: {self.ligado}  Canal: {self.canal}  Volume: {self.volume}')


televisao = Televisor()
televisao.imprimir()
