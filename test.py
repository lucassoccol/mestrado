import vagalume
import matplotlib.pyplot as plt
import formigas
import numpy as np
import time


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

def exec_test_vagalume(populacao, iteracoes):
    custo_vagalumes = []
    avg_vagalume = 0
    start_time_vag = time.time()
    custo_vagalumes = vagalume.main(populacao, iteracoes)
    
    print("--- %s tempo de execucao vagalume em segundos ---" % (time.time() - start_time_vag))
    print('custo dos vagalumes: ', custo_vagalumes)
    avg_vagalume = sum(custo_vagalumes) / float(len(custo_vagalumes))
    print(avg_vagalume)
    print('custo medio vagalumes: ', avg_vagalume)
    print()
    return custo_vagalumes

def exec_test_formiga(populacao, iteracoes):
    custo_formigas = []
    avg_formiga = 0
    start_time_form = time.time()

    custo_formigas = formigas.main(populacao, iteracoes)
    print("--- %s tempo de execucao formigas em segundos ---" % (time.time() - start_time_form))
    print('custo das formigas: ', custo_formigas)
    avg_formiga = sum(custo_formigas) / float(len(custo_formigas))
    print('custo medio formigas: ', avg_formiga)
    print()
    return custo_formigas 
    
def exec_test(populacao, iteracoes):
    plota (iteracoes, populacao, exec_test_vagalume(populacao, iteracoes) , exec_test_formiga(populacao, iteracoes))

def teste_more_pop(cidades):
    populacao = 100
    iteracoes = 10
    exec_test(populacao, iteracoes)

def teste_more_iter(cidades):
    populacao = 10
    iteracoes = 100
    exec_test(populacao, iteracoes)

def teste_equal_50(cidades):
    populacao = 50
    iteracoes = 50
    exec_test(populacao, iteracoes)

def teste_equal_100(cidades):
    populacao = 100
    iteracoes = 100
    exec_test(populacao, iteracoes)  

def teste_city():
    teste_more_pop(15)
    teste_more_iter(15)
    teste_equal_50(15)
    teste_equal_100(15)



def main():
    teste_city()
    
main ()
