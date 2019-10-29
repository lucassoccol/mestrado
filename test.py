import vagalume
import matplotlib.pyplot as plt
import formigas
import numpy as np


#plota as informacoes
def plota(iteracoes, populacao, custo_formigas, custo_vagalumes):
    
    x = range(0, iteracoes)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.xticks(range(0, iteracoes, 5))
    plt.plot(x, custo_formigas)
    plt.plot(x, custo_vagalumes)
    for i,j in zip(x,custo_formigas):
        ax.annotate(str(j),xy=(i,j))

        '''if j == min(custo_formigas):
            circle3 = plt.Circle((i, j), 1 , color='g', clip_on=False)
            ax.add_artist(circle3)'''

        
    for i,j in zip(x,custo_vagalumes):
        ax.annotate(str(j),xy=(i,j))
    plt.title(str(populacao)+ ' populacao x '+ str(iteracoes) +' iteracoes.')
    plt.show()

def teste_more_pop(cidades):
    populacao = 100
    iteracoes = 10
    custo_vagalumes = []
    custo_vagalumes = vagalume.main(populacao, iteracoes)
    print(custo_vagalumes)
    
    
    custo_formigas = []
    custo_formigas = formigas.main(populacao, iteracoes)
    print(custo_formigas)

    plota(iteracoes, populacao, custo_formigas, custo_vagalumes)

def teste_more_iter(cidades):
    populacao = 10
    iteracoes = 100
    custo_vagalumes = []
    custo_vagalumes = vagalume.main(populacao, iteracoes)
    print(custo_vagalumes)
    
    
    custo_formigas = []
    custo_formigas = formigas.main(populacao, iteracoes)
    print(custo_formigas)

    plota(iteracoes, populacao, custo_formigas, custo_vagalumes)

def teste_equal_50(cidades):
    populacao = 50
    iteracoes = 50
    custo_vagalumes = []
    custo_vagalumes = vagalume.main(populacao, iteracoes)
    print(custo_vagalumes)
    
    
    custo_formigas = []
    custo_formigas = formigas.main(populacao, iteracoes)
    print(custo_formigas)

    plota(iteracoes, populacao, custo_formigas, custo_vagalumes) 

def teste_equal_100(cidades):
    populacao = 100
    iteracoes = 100
    custo_vagalumes = []
    custo_vagalumes = vagalume.main(populacao, iteracoes)
    print(custo_vagalumes)
    
    
    custo_formigas = []
    custo_formigas = formigas.main(populacao, iteracoes)
    print(custo_formigas)

    plota(iteracoes, populacao, custo_formigas, custo_vagalumes)    

def teste_city_15():
    teste_more_pop(15)
    teste_more_iter(15)
    teste_equal_50(15)
    teste_equal_100(15)

def teste_city_26():
    teste_more_pop(26)
    teste_more_iter(26)
    teste_equal_50(26)
    teste_equal_100(26)

def teste_city_42():
    teste_more_pop(42)
    teste_more_iter(42)
    teste_equal_50(42)
    teste_equal_100(42)

def main():
    #teste_city_15()
    teste_city_26()
    #teste_city_42
    
main ()