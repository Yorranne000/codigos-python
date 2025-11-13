
from random import random

#tabuleiro do jogo 10x10
tabuleiro=[]
for i in range(10):
    linha=[]
    for j in range(10):
        linha.append(0)
    tabuleiro.append(linha)


contador=0
tentativas_restantes=30
total_de_celulas_do_navio=17 

#Porta-Aviões(5) #Encouraçado(4) #Submarino(3)
#Contratorpedeiro (1)

#posição dos navios
#tamanho do navio e unidade dele

frotas= [[5,1],[4,1],[3,2],[2,1]]
#tamanho_navio
navios=[] #para guardar os navios 

# h v
# 0 = agua 
# n pode ultrapassar o limite do tabuleiro
#posicionar os barcos

