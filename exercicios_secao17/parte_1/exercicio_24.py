"""
24) Baseando-se no exercicio 23 adicione os métodos canalAcima e
canalAbaixo, sendo que o método canalAcima deve sintonizar sempre
o próximo canal em relaão ao canal atual, onde ao chegar ao maior
canal possível deverá voltar ao canal 1. O método canalAbaixo deve
sintonizar sempre o canal anterior em relação ao canal atual, onde
ao chegar ao canal 1 deverá voltar ao maior canal possível, simulando
desta forma o funcionamento de um televisor.
"""


class Televisor:
    def __init__(self):
        self.ligado = True
        self.canal = 1
        self.volume = 1
        self.n_canais = 20
        self.volume_max = 50

    def mostra_canal(self):
        print(f'Canal: {self.canal}')

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


televisao = Televisor()

print()
televisao.mostra_canal()

print('Voltar canal:')
televisao.canal_abaixo()
televisao.mostra_canal()

print('Avançar canal:')
televisao.canal_acima()
televisao.mostra_canal()



