from itertools import permutations
import random
import math
import matplotlib.pyplot as plt
import numpy


cidades = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

melhor_caminho = {'distancia': 100000, 'caminho': []}

distancias = """
0   4   5   6   11  13  20  2   60  16  20
4   0   3   6   7   11  34  23  6   90  10 
5   3   0   3   8   8   40  17  22  21  5
6   6   3   0   11  9   33  2   1   15  74
11  7   8   11  0   4   88  77  93  11  14 
13  11  8   9   4   0   12  14  22  1   36
20  34  40  33  88  12  0   81  20  17  20
2   23  17  2   77  14  81  0   27  54  10
60  6   22  1   93  22  20  27  0   99  55 
16  90  21  15  11  1   17  54  99  0   11
"""

aux = [x.split() for x in distancias.splitlines()[1:]]
matriz = [[int(j) for j in vetor] for vetor in aux]

v = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

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
    path_list.insert(0, 'a')
    path_list.append('a')
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
            b = 1
            # calcula distancia
            r =  _swap_count(vetor[i], vetor[j]) 
            if (retorna_custo(vetor[i]) > (retorna_custo(vetor[j]) * b)):                
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
    for v in vagalumes:
        print(v, "-- custo/brilho: ", retorna_custo(v))

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
    

                
def main():
    n_vagalumes = int(input('Numero de vagalumes: '))
    iteracoes   = int(input('Informe o numero de iteracoes: '))
    cust_vetor = []

    vagalumes = gera_vagalumes(n_vagalumes)
    _draw(vagalumes)
    
    for i in range (iteracoes):
        compara_vagalumes(vagalumes)
        print('-----------------------------', i+1, 'loop -----------------------------------')
        _draw(vagalumes)   
        cust_vetor.append(retorna_custo(vagalumes[min_vag(vagalumes)]))
        print(retorna_custo(vagalumes[min_vag(vagalumes)]))
    
    plota(iteracoes, cust_vetor, n_vagalumes)

    
    
    

 
main()






    

