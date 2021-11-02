# Descrição do Problema
# Conside o seguinte:

# Felipe começa na posição 0km.
# Felipe consegue guardar uma quantidade infinita de água na sua garrafa.
# A cada 1km andado, 1L de água será consumido.
# Felipe não consegue andar adiante com 0L de água.
# Se Felipe chegar no destino com 0L ou mais de água, a jornada é considerada concluída. Da mesma forma, se Felipe chegar em uma parada com 0L de água, ele pode reabastecer.
# Quando para e reabastece, Felipe leva toda a água disponível no local.
# Felipe não é obrigado a reabastecer em parada nenhuma.
# Nenhuma parada ocupa o mesmo lugar que outra.
# As paradas serão dadas em ordem crescente de distância.
# Você deve encontrar, se possível, a menor quantidade de paradas necessárias para se chegar ao destino. Podem haver mais de uma combinação de paradas que chegue ao destino, inclusive mais de uma combinação com o mínimo tamanho possível. Você só precisa descobrir qual é esse tamanho.

# A entrada seguirá o seguinte formato:

# DESTINO AGUA_INICIAL -> Felipe deve caminhar DESTINO kilômetros com AGUA_INICIAL litros iniciais.
# N -> Número N de paradas no meio do caminho.
# Logo ápos virão N linhas da forma:
# POSi CAPi -> Posição da i-ésima parada(POSi) e a quantidade de água disponível na parada (CAPi).
# Constraints
# 1 <= DESTINO <= 4 * 1e6
# 1 <= AGUA_INICIAL <= 8 * 1e5
# 1 <= N <= 8 * 1e5
# 1 <= POSi < DESTINO
# 0 <= CAPi <= 8 * 1e5

import sys
def quick(lista, ini, f):
    if len(lista) == 1:
        return lista #eh pivo
    if ini < f:
        posicao = part(lista, ini, f) #posicao do pivo
        quick(lista, ini, posicao - 1) #o fim eh o pivo - 1
        quick(lista, posicao + 1, f)

def part(lista, inicio, fim):
    pivo = lista[fim][1] #ordenando a qtd de agua
    index = inicio - 1#barra amarela
    for j in range(inicio, fim): #j barra roxa
        if lista[j][1] <= pivo:
            index = index + 1
            lista[index], lista[j] = lista[j], lista[index]
    #trocar a posicao do pivo botando ele no meio
    lista[index+1], lista [fim] = lista[fim], lista[index+1]
    return index+1

def main():

    felipe, felipe_agua = input().split() #um input eu vou pegar a linha inteira
    felipe = int(felipe)
    felipe_agua = int(felipe_agua)
    n = int(input()) 
    lista = []
    #lista ordenada da qtd de água (do maior, para o menor)
    for i in range(n): #quantidade de linhas que vai ter abaixo dos primeiros valores (2ª linha)
        linha1, linha2 = input().split() #linha1 = posição, linha2 = qtd de agua
        aux = [int(linha1), int(linha2)]
        lista.append(aux) #colocando tudo nessa lista
    quick(lista, 0, len(lista) - 1)
    lista.reverse()

    fim = False
    w = 0
    qtd_parada = 0

    while True:
        if felipe <= felipe_agua:
            print('E preciso no minimo {} paradas para chegar no destino.'.format(qtd_parada))
            fim = True
            return fim
        elif w < len(lista):
            if lista[w][0] <= felipe_agua:
                qtd_parada = qtd_parada +1
                felipe_agua = felipe_agua + lista[w][1]
                del(lista[w])
                w = 0 #zerando a variavel
            else:
                w = w + 1 #se a posicação é menos que a quantidade de agua, eu vou incrementar, indo para onde tem mais agua
        else:
            return fim
            
    
if __name__ == '__main__':
    felipe = main()
    if felipe == False:
        print("Nao e possivel chegar no destino, RIP.")