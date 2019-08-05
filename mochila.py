#!/usr/bin/env python3

from itertools import combinations

item = [[4,12], [2,2], [1,1], [10,4], [2,1]]
precos = [4, 2, 1, 10, 2]
pesos  = [12, 2, 1, 4, 1]
bolsa = []
s = 0
c = 0
cm = 0
pesomax = 15

combinado = []

# combina os itens
for i in range (2, len(item)+1):
    for j in combinations(item,i):
        combinado.append(j)

# for x in combinado:
#     print (x)

# coloca na bolsa os que pesam ate 15kg
for i in range(len(combinado)):
    for j in range(len(combinado[i])):
        for k in range(len(combinado[j])):
            # print ("linha: ", i, "grupo: ", j, "elemento: ", k, "valor: ", combinado[i][j][k])
            if k == 1:
                s += combinado[i][j][k]
    # print(s)
    if s <= pesomax :
        bolsa.append(combinado[i])
    s = 0    

# avalia os que possuem o melhor custo
for i in range(len(bolsa)):
    for j in range(len(bolsa[i])):
        for k in range(len(bolsa[j])):
            if k == 0:
                c += bolsa[i][j][k]
    if c > cm :
        cm = i
    c = 0

print (item)

print ("combinacao com maior valor: ",bolsa[cm])

# print (len(combinado[25]))
# print (combinado[25]) = ([4, 12], [2, 2], [1, 1], [10, 4], [2, 1])
# print (combinado[25][0]) = [4, 12]
# print (combinado[25][0][0]) = 4
# print (combinado[25][0][1]) = 12

