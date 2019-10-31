import numpy as np
import math
from bisect import bisect

# Caso queira dar nomes para as cidades (adaptar uso da matriz depois)
# cidades = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

melhor_caminho = {'distancia': math.inf, 'caminho': []}

with open('data//city48.txt') as f:
    w, h = [int(x) for x in next(f).split()]
    matriz = [[int(x) for x in line.split()] for line in f]

cidades = list(range(0, w))
np.set_printoptions(precision=5, linewidth=100)
matriz_feromonios = np.ones((w, w))

alpha = 1 #int(input('Valor do Alpha(padrão 1): ') or "1")
betta = 1 #int(input('Valor do Betta(padrão 1): ') or "1")
taxa_evaporacao = 0.5 #float(input('Taxa de Evaporação (padrão 0.5): ') or "0.5")


def evaporar_feromonios():
    global matriz_feromonios
    matriz_feromonios = matriz_feromonios * taxa_evaporacao


def calcula_custos(cidade_atual, cidades_para_visitar):
    relacao_distancias = {}
    for cidade_destino in cidades_para_visitar:
        relacao_distancias[cidade_destino] = matriz[cidade_atual][cidade_destino]
    return relacao_distancias


def obtem_feromonios(cidade_atual, cidades_para_visitar):
    relacao_feromonios = {}
    for cidade_destino in cidades_para_visitar:
        relacao_feromonios[cidade_destino] = matriz_feromonios[cidade_atual][cidade_destino]
    return relacao_feromonios


def calcula_probabilidades(feromonios_totais, custos_totais):
    n = 1 / custos_totais
    total = np.sum((feromonios_totais ** alpha) * (n ** betta))
    return ((feromonios_totais ** alpha) * (n ** betta)) / total


def roleta(probabilidades, argsort):
    numero_aleatorio = np.random.rand()
    soma_acumulada = np.cumsum(probabilidades)
    posicao = bisect(soma_acumulada, numero_aleatorio)
    return argsort[posicao]


def percorrer_caminho(caminho, custo):
    global matriz_feromonios
    for i in range(len(caminho) - 1):
        matriz_feromonios[caminho[i]][caminho[i+1]] += 1/custo
        matriz_feromonios[caminho[i+1]][caminho[i]] += 1/custo


def atualiza_melhor_caminho(caminho, custo):
    global melhor_caminho
    if custo < melhor_caminho['distancia']:
        melhor_caminho['distancia'] = custo
        melhor_caminho['caminho'] = caminho

def main (numero_formigas, iteracoes):
    custos = []
    for iteracao in range(iteracoes):
        caminhos_por_formiga = []
        custos_por_formiga = []
        evaporar_feromonios()
        for formiga in range(numero_formigas):
            cidades_visitar = cidades[1:]
            cidade_inicial = 0
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
                cidades_visitar.remove(cidade_atual)
            custo += matriz[cidades[caminho[-1]]][cidades[cidade_inicial]]
            caminho.append(cidade_inicial)
            caminhos_por_formiga.append(caminho)
            custos_por_formiga.append(custo)
            atualiza_melhor_caminho(caminho, custo)
        for caminho, custo in zip(caminhos_por_formiga, custos_por_formiga):
            percorrer_caminho(caminho, custo)
           
        custos.append(min(custos_por_formiga))
    return custos
