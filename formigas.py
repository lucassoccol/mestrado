import numpy as np
from bisect import bisect

cidades = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

melhor_caminho = {'distancia': 100000, 'caminho': []}


distancias_totais = """
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
np.set_printoptions(precision=5, linewidth=100)
aux = [x.split() for x in distancias_totais.splitlines()[1:]]
matriz = [[int(j) for j in vetor] for vetor in aux]

matriz_feromonios = np.ones((10, 10))

iteracoes = 10
alpha = 1
betta = 1
numero_formigas = 5
taxa_evaporacao = 0.5
formigas = 10


def evaporar_feromonios():
    global matriz_feromonios
    matriz_feromonios = matriz_feromonios * taxa_evaporacao


def calcula_custos(cidade_atual, cidades_para_visitar):
    relacao_distancias = {}
    for cidade_destino in cidades_para_visitar:
        relacao_distancias[cidade_destino] = matriz[cidades[cidade_atual]][cidades[cidade_destino]]
    return relacao_distancias


def obtem_feromonios(cidade_atual, cidades_para_visitar):
    relacao_feromonios = {}
    for cidade_destino in cidades_para_visitar:
        relacao_feromonios[cidade_destino] = matriz_feromonios[cidades[cidade_atual]][cidades[cidade_destino]]
    return relacao_feromonios


def calcula_probabilidades(feromonios_totais, custos_totais):
    n = 1 / custos_totais
    total = np.sum((feromonios_totais ** alpha) * (n ** betta))
    return ((feromonios_totais ** alpha) * (n ** betta)) / total


def roleta(probalidades, argsort):
    numero_aleatorio = np.random.rand()
    # print(f'numero aleatorio {numero_aleatorio}')
    soma_acumulada = np.cumsum(probalidades)
    # print(f'soma acumulada {soma_acumulada}')
    posicao = bisect(soma_acumulada, numero_aleatorio)
    # print(f'posicao {argsort[posicao]}')
    return argsort[posicao]


def percorrer_caminho(caminho, custo):
    global matriz_feromonios
    for i in range(len(caminho) - 1):
        matriz_feromonios[cidades[caminho[i]]][cidades[caminho[i+1]]] += 1/custo
        matriz_feromonios[cidades[caminho[i+1]]][cidades[caminho[i]]] += 1/custo


def atualiza_melhor_caminho(caminho, custo):
    global melhor_caminho
    if custo < melhor_caminho['distancia']:
        melhor_caminho['distancia'] = custo
        melhor_caminho['caminho'] = caminho


for iteracao in range(iteracoes):
    print()
    print(f'Iniciando iteração número {iteracao}')
    caminhos_por_formiga = []
    custos_por_formiga = []
    print(f'Evaporando feromônios com fator p de {taxa_evaporacao}')
    evaporar_feromonios()
    for formiga in range(formigas):
        print()
        print(f'Iniciando percurso para formiga {formiga + 1}')
        cidades_visitar = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        cidade_inicial = 'a'
        cidade_atual = cidade_inicial
        caminho = [cidade_inicial]
        custo = 0
        while cidades_visitar:
            distancias_totais = calcula_custos(cidade_atual, cidades_visitar)
            feromonios_totais = obtem_feromonios(cidade_atual, cidades_visitar)
            probabilidades_cidades = calcula_probabilidades(np.array(list(feromonios_totais.values())),
                                                            np.array(list(distancias_totais.values())))
            probabilidades_cidades_ordenado = np.sort(probabilidades_cidades)
            ordem_original = np.argsort(probabilidades_cidades)
            cidade_escolhida_index = roleta(probabilidades_cidades_ordenado, ordem_original)
            cidade_atual = list(distancias_totais)[cidade_escolhida_index]
            caminho.append(cidade_atual)
            custo += list(distancias_totais.values())[cidade_escolhida_index]
            print(f'cidade escolhida: {list(distancias_totais)[cidade_escolhida_index]}. Custo: {custo}')
            cidades_visitar.remove(cidade_atual)
        custo += matriz[cidades[caminho[-1]]][cidades[cidade_inicial]]
        caminho.append(cidade_inicial)

        # print(f'Caminho encontrado: {caminho}')
        # print(f'Custo: {custo}')
        caminhos_por_formiga.append(caminho)
        custos_por_formiga.append(custo)
        atualiza_melhor_caminho(caminho, custo)

    print()
    for caminho, custo in zip(caminhos_por_formiga, custos_por_formiga):
        print(f"caminho {caminho} e custo {custo}")
        percorrer_caminho(caminho, custo)

    # print(matriz_feromonios)
print()
print(melhor_caminho)
