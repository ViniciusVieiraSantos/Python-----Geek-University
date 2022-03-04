"""
4) Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o
volume e trocar os canais da televisão.
    . O controle de volume permite aumentar ou diminuir a potência do volume
    de som em uma unidade de cada vez;
    . O controle de canal tambpem permite aumentar e diminuir o número do canal em
    uma unidade, porém, também possibilita trocar para um canal indicado;
    . Também devem existir métodos para consultar o valor do volume de som e o
    canal selecionado.
"""


class Televisao:
    def __init__(self, canal=1, volume=1):
        self.canal = canal
        self.volume = volume

    def get_canal(self):
        return self.canal

    def set_canal(self, valor):
        self.canal = valor

    def controla_volume(self, valor):
        if 0 <= self.volume + valor <= 10:
            self.volume += valor
        elif self.volume + valor > 10:
            self.volume = 10
        else:
            self.volume = 0
        print(f'Volume : {self.volume}')

    def controla_canal(self, valor):
        if 1 <= self.canal + valor <= 8:
            self.canal += valor
        elif self.canal + valor > 8:
            self.canal = 1
        else:
            self.canal = 8
        print(f'Canal : {self.canal}')


class ControleRemoto:
    def __init__(self, televisao):
        self.televisao = televisao

    def aumenta_volume(self):
        self.televisao.controla_volume(+1)

    def diminui_volume(self):
        self.televisao.controla_volume(-1)

    def aumenta_canal(self):
        self.televisao.controla_canal(+1)

    def diminui_canal(self):
        self.televisao.controla_canal(-1)

    def troca_canal(self, valor):
        if 0 < valor < 20:
            print(valor)
            self.televisao.set_canal(valor)
        else:
            print(f'ERRO')

    def mostra_volume(self):
        print(f'Volume : {self.televisao.volume}')

    def mostra_canal(self):
        print(f'Canal : {self.televisao.canal}')


tv = Televisao()
ct = ControleRemoto(tv)
ct.diminui_volume()
ct.aumenta_volume()
ct.diminui_canal()
ct.aumenta_canal()
ct.mostra_canal()
ct.mostra_volume()
