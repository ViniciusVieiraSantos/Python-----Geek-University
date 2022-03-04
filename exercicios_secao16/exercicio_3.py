"""
3) Crie uma classe denominada Elevador para armazenar as informações de um
elevador dentro de um prédio. A classe deve armazenar o andar atual (térreo = 0),
total de andares no prédio, excluindo o térreo, capacidade do elevador, e
quantas pessoas estão presentes nele.
A classe deve também disponibilizar os seguintes métodos:
    . Inicializa: que deve receber como parâmetros a capacidade do elevador e
    o total de andares no prédio (os elevadores sempre começam no térreo vazio);
    . Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda
    houver espaço);
    . Sai: para remover uma pessoa do elevador (só deve remover se houver alguém
    dentro dele);
    . Sobe: para subir um andar (não deve subir se já estiver no último andar);
    . Desce: para descer um andar (não deve descer se já estiver no térreo);
    . Encapsular todos os atributos da classe (criar métodos set e get).
"""


class Elevador:

    def __init__(self, andares, capacidade):
        self.andares = andares
        self.capacidade = capacidade
        self.pessoas = 0
        self.andar_atual = 0

    def entra(self):
        if self.pessoas < self.capacidade:
            self.pessoas += 1
            print(f'Uma pessoa entrou. A quantidade de pessoas no elevador é {self.pessoas}.')
        else:
            print('Capacidade maxima atingida.')

    def sai(self):
        if self.pessoas > 0:
            self.pessoas -= 1
            print(f'Uma pessoa saiu. A quantidade de pessoas no elevador é {self.pessoas}.')
        else:
            print('O elevador já está vazio.')

    def sobe(self):
        if self.andar_atual < self.andares:
            self.andar_atual += 1
            print(f'O elevador subiu 1 andar. O elevador está no andar {self.andar_atual}.')
        else:
            print('O elevador já esta no último andar.')

    def desce(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print(f'O elevador desceu 1 andar. O elevador está no andar {self.andar_atual}.')
        else:
            print('O elevador está no terréo.')

    @property
    def andares(self):
        return self._andares

    @andares.setter
    def andares(self, andar):
        if isinstance(andar, str):
            andar = int(andar)

        self._andares = andar

    @property
    def capacidade(self):
        return self._capacidade

    @capacidade.setter
    def capacidade(self, c):
        if isinstance(c, str):
            c = int(c)

        self._capacidade = c


elevador1 = Elevador(3, 6)
elevador1.desce()
elevador1.sai()
elevador1.sobe()
elevador1.sobe()
elevador1.sobe()
elevador1.sobe()
elevador1.entra()
elevador1.entra()
elevador1.entra()
elevador1.entra()
elevador1.entra()
elevador1.entra()
elevador1.entra()
