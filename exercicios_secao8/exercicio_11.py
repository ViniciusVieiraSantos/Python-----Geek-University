"""
11) Elabore uma função que receba três notas de um aluno como parâmetros e
uma letra. Se a letra for A, a função deverá calcular a média aritmética das
notas do aluno; se for P, deverá calcular a média ponderada, com pesos 5, 3, e 2.
"""


def calcular_notas(nota_1, nota_2, nota_3, letra):
    if letra == 'A':
        media = (nota_1 + nota_2 + nota_3) / (nota_1 + nota_2 + nota_3)
        return print(f'Média aritmética : {round(media, 1)}')

    elif letra == 'P':
        media = (nota_1 * 5 + nota_2 * 3 + nota_3 * 2) / (nota_1 + nota_2 + nota_3)
        return print(f'Média ponderada : {round(media, 1)}')

    return print('Letra digitida invalida')


a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a  terceira nota: "))
d = str(input("Digite 'A' para calcular media aritmética ou 'P' para calcular média ponderada: ")).upper()
