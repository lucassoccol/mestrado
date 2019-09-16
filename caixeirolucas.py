from itertools import permutations

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

def funcao_objetivo(sequencia_cidades):
    custo_caminho = 0
    print(sequencia_cidades)
    for i in range(len(sequencia_cidades) - 1):
        custo_caminho += matriz[cidades[sequencia_cidades[i]]][cidades[sequencia_cidades[i+1]]]
    if custo_caminho < melhor_caminho['distancia']:
        melhor_caminho['distancia'] = custo_caminho
        melhor_caminho['caminho'] = sequencia_cidades
    return custo_caminho


def create_paths():
    result = []
    for path in permutations('bcdefghij', 9):
        path_list = list(path)
        path_list.insert(0, 'a')
        path_list.append('a')
        result.append(path_list)
        print(path_list)
    return result


list(map(funcao_objetivo, create_paths()))
print(melhor_caminho)
