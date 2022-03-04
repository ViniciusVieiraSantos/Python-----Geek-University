"""
39) Faça uma função 'Troque', que recebe duas variáveis reais A e B
e troca o valor delas (i.e., A recebe o valor de B e B recebe o valor de A).
"""


def troque(numero_1, numero_2):
    return numero_2, numero_1


a = float(input('Digite um numero : '))
b = float(input('Digite um numero : '))

a, b = troque(a, b)
print(a, b)
