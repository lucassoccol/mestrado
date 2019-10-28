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


def main():
    populacao = int(input('Informe a quantidade de populacao: '))
    iteracoes = int(input('Informe a quantidade de iteracoes: '))

    custo_vagalumes = []
    custo_vagalumes = vagalume.main(populacao, iteracoes)
    print(custo_vagalumes)
    
    
    custo_formigas = []
    custo_formigas = formigas.main(populacao, iteracoes)
    print(custo_formigas)

    plota(iteracoes, populacao, custo_formigas, custo_vagalumes)

main ()