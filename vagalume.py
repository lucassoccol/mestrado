from itertools import permutations
import random
import math
import matplotlib.pyplot as plt
import numpy

with open('data//city48.txt') as f:
    w, h = [int(x) for x in next(f).split()]
    matriz = [[int(x) for x in line.split()] for line in f]

cidades = list(range(0, w))

v = []
for z in range (1, len(cidades)):
    v.append(cidades[z])

#funcao obj e retorno de brilho
def retorna_custo(sequencia):
    custo = 0
    for i in range(len(sequencia)-1):
        custo+= matriz[cidades[sequencia[i]]][cidades[sequencia[i+1]]]
    return custo

#gera um vagalume
def gen_vag ():
    random.shuffle(v)
    path_list = list(v)
    path_list.insert(0, 0)
    path_list.append(0)
    return path_list

#gere a populacao inicial de vagalumes aleatoriamente
def gera_vagalumes (qtde):
    vetor = []
    for i in range(qtde):
        vetor.append(gen_vag())
    return vetor

#gera uma população otimizada com custo max e min
def gen_vag_otm (qtd, c_max, c_min):
    aleatorio = []
    for i in range (math.factorial(len(v)-1)):
        aux = gen_vag()
        if (retorna_custo(aux) <= c_max) and (retorna_custo(aux) >= c_min):
            aleatorio.append(aux)
            break
    return aleatorio

#retorno o indice com menor custo
def min_vag (vetor):
    custo = []
    for v in vetor:
        custo.append(retorna_custo(v))
    return custo.index(min(custo))

#troca posicao no vetor
def change (vetor, posa, posb):
    aux = vetor[posa]
    vetor[posa] = vetor[posb]
    vetor[posb] = aux

#faz os swap para igualar os vetores
def _swap(vetora, vetorb, q_swap):
    sc = 0 
    for i in range(1, len(vetorb)-1):
        if not vetorb[i] == vetora[i] and sc < q_swap:
            sc += 1         
            change(vetora, i, vetora.index(vetorb[i]))

#faz a contagem de swaps
def _swap_count(vetora, vetorb):
    sc = 0 
    for i in range(1, len(vetorb)-1):
        if not vetorb[i] == vetora[i]:
            sc += 1
    return sc

#comparar todos com todos e if (xi < xj) xi movimenta-se para xj // calcula distancia xj - xi
def compara_vagalumes (vetor):
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            aleatorio = vetor[i].copy()
            #fator de atratividade
            b = 0.2
            # calcula distancia
            r =  _swap_count(vetor[i], vetor[j])

            if b > 0:
                prox_vag = retorna_custo(vetor[j]) * b
            else:
                prox_vag = retorna_custo(vetor[j])

            if (retorna_custo(vetor[i]) > prox_vag):
                if r > 0:
                    _swap(aleatorio, vetor[j], (random.randrange(0, r, 2)))       
                    if retorna_custo(aleatorio) <= retorna_custo(vetor[i]):
                        vetor[i] = aleatorio
            else:
                    #for k in range(len(v)):
                change(aleatorio, random.randrange(1, (len(v)), 1), random.randrange(1, (len(v)), 1))
                        #if (retorna_custo(vetor[i]) > (retorna_custo(aleatorio))):
                vetor[i] = aleatorio



#printa populacao 
def _draw (vagalumes):
    for vag in vagalumes:
        print(vag, "-- custo/brilho: ", retorna_custo(vag))

#plota as informacoes
def plota(iteracoes, cust_vetor, n_vagalumes):

    x = range(0, iteracoes)
    y = cust_vetor

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.xticks(range(0, iteracoes, 5))
    plt.plot(x,y)
    for i,j in zip(x,y):
        ax.annotate(str(j),xy=(i,j))
    plt.title(str(n_vagalumes)+ ' vagalumes.')
    plt.show()    
    

                
def main(populacao, iteracoes):
    n_vagalumes = populacao
    iteracoes   = iteracoes
    cust_vetor = []

    #print(cidades)
    #print(v)

    vagalumes = gera_vagalumes(n_vagalumes)

    #print(vagalumes)
    #_draw(vagalumes)
    
    for i in range (iteracoes):
        compara_vagalumes(vagalumes)
        #print('-----------------------------', i+1, 'loop -----------------------------------')
        #_draw(vagalumes)   
        cust_vetor.append(retorna_custo(vagalumes[min_vag(vagalumes)]))
        #print(retorna_custo(vagalumes[min_vag(vagalumes)]))
    
    #plota(iteracoes, cust_vetor, n_vagalumes)

    return cust_vetor





 






    

