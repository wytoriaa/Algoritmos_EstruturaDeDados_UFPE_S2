# Para conseguir lucrar o máximo possível, Marie falou para você montar o combo da seguinte forma:

# O combo deve ter N itens.
# Os N itens devem ser os mais caros da loja.
# Para cada item i cujo preço é P reais, o valor do item no combo será de P-1 reais.
# Dada uma lista dos preços dos produtos, você deve retornar para Marie o indice dos produtos escolhidos 
# e o valor total do combo.

# Algumas observações:

# É garantido que N é menor ou igual ao total de produtos da loja
# Todos os produtos possuem preços distintos
#fazer a questao no estilo dividir para conquistar
import sys
def quick(lista, ini, f):
    if len(lista) == 1:
        return lista #eh pivo
    if ini < f:
        posicao = part(lista, ini, f) #posicao do pivo
        quick(lista, ini, posicao - 1) #o fim eh o pivo - 1
        quick(lista, posicao + 1, f)

def part(lista, inicio, fim):
    pivo = lista[fim][0]
    index = inicio - 1#barra amarela
    for j in range(inicio, fim): #j barra roxa
        if lista[j][0] <= pivo:
            index = index + 1
            lista[index], lista[j] = lista[j], lista[index]
    #trocar a posicao do pivo botando ele no meio
    lista[index+1], lista [fim] = lista[fim], lista[index+1]
    return index+1

def main():
    start = []
    try: 
        for line in sys.stdin:
            start.append(line)
    except:
        pass

    partida = start[0].split()
    t = int(partida[0])
    n = int(partida[1])
    combo = []

    for i in range(1, t+1): 
        produtos = [int(start[i]), i - 1] #a linha comeca vazia
        combo.append(produtos)
         
    quick(combo, 0, len(combo) - 1)
    combo.reverse() #reverse() eh usado para reverter os elementos da lista
    pegaResult = ""
    prc = 0 #inicia com zero
      
    for i in range(n):
        produtos = combo[i][0] #pega indice zero
        pos = combo[i][1]
        pegaResult = pegaResult + str(pos) + " "
        prc = prc + produtos - 1
    pegaResult = pegaResult.strip() #adiciona uma linha a matriz
    print("O combo vai custar {} reais, e os produtos escolhidos foram: {}".format(prc, pegaResult))
  
if __name__ == '__main__':
    main()