"""
67) Faça uma rotina que receba como parâmetro um vetor de caracteres e
seu tamanho. A função deverá de ler uma string do teclado, caractere por caractere
usando a função getchat() até que o usuário digite enter ou o tamanho máximo do
vetor seja alcançado.
"""


def getchar():
    caractere = input("Informe um caractere: ")

    if len(caractere) <= 1:
        return caractere


def rotina(vetor, tamanho):
    for _ in range(tamanho):
        valor = getchar()
        if valor != '':
            vetor.append(valor)
        else:
            break
    print(vetor)


v = []
tam = 5

rotina(v, tam)
