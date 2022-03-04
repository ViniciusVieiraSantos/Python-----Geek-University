"""
21) Basenado-se no exercício 20 adicione um método construtor que
permita a definição de todos os atributos no momento da instanciação do
objeto.
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
