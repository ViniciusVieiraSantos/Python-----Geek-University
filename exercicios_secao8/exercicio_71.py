"""
71) Considerando a estrutura:
    struct Ponto{
    int x;
    int y;
    };
Para representar um ponto em uma grade 2D, implemente uma função que indique se um
ponto p está localicado dentro ou fora de um retângulo. O retângulo é definico
por seus vértices inferior esquerdo v1 e superior direito v2. A função deve retornar
1 caso o ponto esteja localizado dentro do retângulo e 0 caso contrário. Essa função deve
obedecer ao protótipo:
int dentroRet (struct Ponto* v1, struct Ponto* v2, struct Ponto* p);
"""


def verifica_ponto(vertice_1, vertice_2, ponto):
    if ponto[0] < vertice_1[0] or ponto[0] > vertice_2[0] or ponto[1] < vertice_1[1] or ponto[1] > vertice_2[1]:
        return 0
    return 1


v1 = []
v2 = []
p = []

print('Digite os 2 pontos do vertice inferior esquerdo do retangulo:')
for i in range(2):
    v1.append(int(input()))

print('Digite os 2 pontos do vertice superior direito do retangulo:')
for i in range(2):
    v2.append(int(input()))

print('Digite os 2 pontos para verificar se encontram dentro do retangulo:')
for i in range(2):
    p.append(int(input()))

print(verifica_ponto(v1, v2, p))
