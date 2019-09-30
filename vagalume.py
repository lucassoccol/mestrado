from itertools import permutations
import random

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

#numero de variaveis de projeto
n_var = 1
n_vagalumes = 5
vagalumes = []

v = ['b', 'c', 'd', 'e', 'f', 'g']

def retorna_custo(sequencia):
    custo = 0
    for i in range(len(sequencia)-1):
        custo+= matriz[cidades[sequencia[i]]][cidades[sequencia[i+1]]]
    return custo
#gere a populacao inicial de vagalumes aleatoriamente

def gera_vagalumes (qtde):
    vetor = []
    for i in range(qtde):
        random.shuffle(v)
        path_list = list(v)
        path_list.insert(0, 'a')
        path_list.append('a')
        #path_list.append(retorna_custo(path_list))
        vetor.append(path_list)
    return vetor

def gen_vag ():
    vetor = []
    random.shuffle(v)
    path_list = list(v)
    path_list.insert(0, 'a')
    path_list.append('a')
    vetor.append(path_list)
    return vetor

def gen_vag_otm (qtd, c_max, c_min):
    aleatorio = []
    for i in range (qtd):
        bo = True
        while bo == True:
            aux = gen_vag()
            if (retorna_custo(aux[0]) < c_max) and (retorna_custo(aux[0]) > c_min):
                aleatorio.append(aux)
                bo = False
    return aleatorio

#comparar todos com todos e if (xi < xj) xi movimenta-se para xj // calcula distancia xj - xi
def compara_vagalumes (vetor):
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if retorna_custo(vetor[i]) > retorna_custo(vetor[j]):
                #mova i para j 
                dif = retorna_custo(vetor[j]) - retorna_custo(vetor[i])
                fat_at = 0.1
                #valor_prox = retorna_custo(vetor[i]+(dif / fat_at))

                aleatorio = gen_vag_otm(n_vagalumes, retorna_custo(vetor[i]), retorna_custo(vetor[j]))

                #min(myList, key=lambda x:abs(x-myNumber))

                for k in range (len(aleatorio)):
                    print("--------------" , k ," ------------")
                    print(aleatorio[k], retorna_custo(aleatorio[k][0]))
                     

def menor_custo (vetor):
    menor = 1000
    for i in range(len(vetor)):
        if retorna_custo(vetor[i]) < menor:
            pos = i
            menor = retorna_custo(vetor[i])
    return vetor[pos]

def main():
    vagalumes = gera_vagalumes(n_vagalumes)
    for v in vagalumes:
        print(v, "-- custo: ", retorna_custo(v))

    compara_vagalumes(vagalumes)


    print("--------------------------")
        
main()

#proximo passo encontrar a menor diferenca no aleatorio e fazer vagalume ir ate ela.












    

