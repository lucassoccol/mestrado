import numpy as np

cidades = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

melhor_caminho = {'distancia': 100000, 'caminho': []}


distancias = """
0   4   5   6   11  13  20  2   60  16  
4   0   3   6   7   11  34  23  6   90
5   3   0   3   8   8   40  17  22  21
6   6   3   0   11  9   33  2   1   15
11  7   8   11  0   4   88  77  93  11
13  11  8   9   4   0   12  14  22  1
20  34  40  33  88  12  0   81  20  17
2   23  17  2   77  14  81  0   27  54
60  6   22  1   93  22  20  27  0   99
16  90  21  15  11  1   17  54  99  0
"""

aux = [x.split() for x in distancias.splitlines()[1:]]
matriz = [[int(j) for j in vetor] for vetor in aux]

matriz_feromonios = np.zeros((10, 10))

alpha = 1
betta = 1
numero_formigas = 5
taxa_evaporacao = 0.5

cidades_visitar = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
cidade_atual = 'a'


def evaporar_feromonios():
    global matriz_feromonios
    matriz_feromonios = matriz_feromonios * taxa_evaporacao


def calcula_custos(cidade_atual, cidades_para_visitar):
    relacao_distancias = {}
    for cidade_destino in cidades_para_visitar:
        relacao_distancias[cidade_destino] = matriz[cidades[cidade_atual]][cidades[cidade_destino]]
    return relacao_distancias


def calcula_probabilidades(feromonios_totais, custos_totais):
    n = 1 / custos_totais
    total = np.sum((feromonios_totais ** alpha) * (n ** betta))
    return ((feromonios_totais ** alpha) * (n ** betta)) / total


feromonios = np.array([1, 1, 1])
custos = np.array([1, 15, 4])


print(calcula_probabilidades(feromonios, custos))
