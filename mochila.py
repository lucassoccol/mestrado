#!/usr/bin/python
#coding: utf-8

from itertools import combinations



# problema da mochila
# colocar o máximo de valor dentro da mochila

def organiza (peso, valor, custo):
	for i in range (len(custo)):
		if i < len(custo)-1:
			# verifica se o custo é menor
			if (custo[i] < custo[i+1]):
				# salva o valor do indice em uma variavel
				auxV = valor [i]
				auxP = peso  [i]
				auxC = custo [i]

				#troca o valor do indice para o valor subsequente
				valor[i] = valor[i+1]
				peso [i] = peso [i+1]
				custo[i] = custo[i+1]

				#valor subsequente recebe os valores maiores
				valor[i+1] = auxV
				peso [i+1] = auxP
				custo[i+1] = auxC

				organiza(peso, valor, custo)



def geracusto (peso, valor):
	custo = []
	for i in range (len(peso)):
		custo.append(valor[i]/peso[i])
	return custo

def poenabolsa (peso, custo, mochila):
 	pesomax = mochila
 	pesoacu = 0
 	for i in range (len(custo)-1):
 		if pesoacu <= pesomax:
 			pesoacu = pesoacu + peso[i]




def main():
	mochila = 15
	itens = [[12,4], [2,2], [1,1], [4,10], [1,2]]
	peso  = [12, 2, 1, 4, 1]
	valor = [4, 2, 1, 10, 2]
	custo = []
	combinado = []

	for i in range (len(itens)+1):
		if i >= 2:
			combinado.append = combinations(itens, i)

	print (combinado)
	custo = geracusto (peso, valor)

	print (peso)
	print (valor)
	print (custo)
	print ("")

	organiza(peso, valor, custo)

	print (peso)
	print (valor)
	print (custo)


main()



