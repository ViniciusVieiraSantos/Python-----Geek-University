"""
72) Considerando a estrutura
    struct Vetor{
    float x;
    float y;
    float z;
    };
para representar um vetor de R³, implemente umaa função que calcule a soma
de dois vetores. Essa função deve obedecer ao protótipo:
void soma (struct Vetor* v1, struct Vetor* v2, struct Vetor* res);
onde os parâmetros v1 e v2 são ponteiros para os vetores a seren somados, e o parâmetro
res é um ponteiro para uma estrutura vetor onde o resultado da operação deve ser
armazenado
"""


def vetor(x, y, z):
    return {'x': x, 'y': y, 'z': z}


x = int(input('Digite o 1º número do Vetor 1: '))
y = int(input('Digite o 2º número do Vetor 1: '))
z = int(input('Digite o 3º número do Vetor 1: '))

dictV1 = vetor(x, y, z)

print()
x = int(input('Digite o 1º número do Vetor 2: '))
y = int(input('Digite o 2º número do Vetor 2: '))
z = int(input('Digite o 3º número do Vetor 2: '))

dictV2 = vetor(x, y, z)


def soma(dict_v1, dict_v2):
    res = []

    for k in dict_v1:
        res.append(dict_v1[k] + dict_v2[k])

    return res


print()
print('Soma dos vetores: ', soma(dictV1, dictV2))

