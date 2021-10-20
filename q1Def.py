#Criando o Nó:
class Node:
    def __init__(self, valor = 0, proximo = None):
        self.value = valor
        self.proximo = None
class Queue:
    def __init__(self):
        self.comeco = None
        self.fim = None
    #para inserir o produto na esteira
    def push(self, node):
        novoNo = node
        if self.comeco == None:
            self.comeco = novoNo
            self.fim = novoNo
        else:
            self.fim.proximo = novoNo
            self.fim = novoNo
    #para remover o produto da esteira
    def pop(self):
        if self.comeco == None:
            print('A esteira ficou vazia!')
        else:
            auxiliar = self.comeco
            self.comeco = auxiliar.proximo
            print("O elemento foi removido: ", auxiliar.valor) 
    #para mover de uma esteira para outra
    def moveEsteira(self):
        temp = self.comeco
        while temp != None:
            print(temp.value)
            temp = temp.proximo

def main():



    #fazendo as leituras
    try:
        produto = int(input())
        criaLista = [0] * produto
        for moveProduto in range (produto):
            criaFilaNova = Queue()
            criaLista[moveProduto] = criaFilaNova
        linha = None
        while linha != 'Fim':
            linha = input()
            produto = linha.split()
            if produto [0] == "RMV":
                try:
                    remover, tamanho = criaLista[int(produto[1]-1)].pop()
                    if tamanho != 0:
                        print('O produto foi adicionado')
                    else:
                        print('Não há produtos na esteira')
                except:
                    pass
            if linha [0] == 'INS':
                    criaLista[int(linha[1])-1].add(linha[2]) #para inserir outro elemento
            if linha [0] == 'SHOW':
                    criaFilaNova[int(linha[1])-1].read(int(linha[1])) #para mostrar
            if linha[0] == 'MOV':
                #a utilização do elif serve para evitar varios if e else no código, fazendo assim com que 
                #diminua as linhas do código, um pouco
                    try:
                        remove, tamanho = linha [int(linha[1])-1].pop()
                        linha[int(linha[2])-1].push(remover)
                        print('O produto foi movido para outra esteira')
                    except:
                        print('Erro na remoção do produto')
    except:
        pass
if __name__ == "__main__":
    main()