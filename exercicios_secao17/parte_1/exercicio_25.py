"""
25) Baseando-se no exercício 24 adicione os métodos volumeAcima
e volumeAbaixo, sendo que o método volumeAcima deve modificar
o volume para o próximo nível de volume possível, onde ao chegar
ao volumeMaximo não poderá possibilitar que o volume seja alterado.
O método volumeAbaixo deve modificar o volume para o nível imediatamente
inferior de volume me relação ao volume atual, não podendo ser menor do
que 0, simulando desta forma o funcionamento de um televisor.
"""


class Televisor:
    def __init__(self):
        self.ligado = True
        self.canal = 1
        self.volume = 1
        self.n_canais = 20
        self.volume_max = 50

    def mostra_volume(self):
        print(f'Volume: {self.volume}')

    def canal_acima(self):
        if self.canal == self.n_canais:
            self.canal = 1
        else:
            self.canal += 1

    def canal_abaixo(self):
        if self.canal == 1:
            self.canal = self.n_canais
        else:
            self.canal -= 1

    def volume_acima(self):
        if self.volume < self.volume_max:
            self.volume += 1

    def volume_abaixo(self):
        if self.volume > 0:
            self.volume -= 1


televisao = Televisor()

print('Volume inicial:')
televisao.mostra_volume()

print('\nAbaixando volume 3x:')
for i in range(3):
    televisao.volume_abaixo()
    televisao.mostra_volume()

print('\nAumentando volume 3 x:')
for i in range(3):
    televisao.volume_acima()
    televisao.mostra_volume()
