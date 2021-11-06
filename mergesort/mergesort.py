# A competição de cada semana vai funcionar da seguinte maneira: 
# Oliver tem N (N sempre é par) alunos e ele quer seperá-los em duplas, 
# onde cada dupla irá lutar entre si. Para manter a comnpetição justa, 
# durante a semana Oliver pontua seus alunos de acordo com seu desempenho durante a semana, 
# e no dia da competição ele enfileira os alunos em ordem crescente de pontuação,
#  e puxa os alunos 2 a 2 para lutar entre si.

# Dada uma lista com a pontuação da semana de cada aluno, 
# você deve retornar uma lista com a diferença de pontos de cada dupla.

def mergeSort(lista):
    if len(lista)>1:
        meio = len(lista)//2
        esq_half = lista[:meio]
        dir_half = lista[meio:]

        mergeSort(esq_half)
        mergeSort(dir_half)

        i=0
        j=0
        k=0
        while i < len(esq_half) and j < len(dir_half):
            if esq_half[i] < dir_half[j]:
                lista[k]=esq_half[i]
                i=i+1
            else:
                lista[k]=dir_half[j]
                j=j+1
            k=k+1

        while i < len(esq_half):
            lista[k]=esq_half[i]
            i=i+1
            k=k+1

        while j < len(dir_half):
            lista[k]=dir_half[j]
            j=j+1
            k=k+1
def main():
    qtd_alunos = int(input()) #qtd de alunos
    pontos = []
    #pontuacao definida em ordem crescente
    #pegar a pontuacao de cada linha do input
    for c in range(qtd_alunos):
        pontos.append(int(input())) #acrescentar pontuacao no final da lista
    mergeSort(pontos)

    #fazendo a diferenca de pontuacao
    def_pontuacao = []
    for i in range(0, qtd_alunos, 2):
        def_pontuacao.append(pontos[i + 1] - pontos[i])
        #pegando o segundo aluno (eh i + 1), e o primeiro [i])
    mergeSort(def_pontuacao) #infileira os alunos em ordem crescente de pontuaçao

    for w in range(len(def_pontuacao)): #printando a diferenca de pontuacao
        print(def_pontuacao[w])

if __name__ == "__main__":
    main()

#baseado na tecnica dividir para conquistar (divider and conquer)
#mergesort = ordernacao (sort) por juncao (merge)
#ele separa nossa lista em dados menores, e depois uni eles de mandeira ordenada

#ex: 
# [4, 7, 2, 6, 4, 1, 8, 3]
#[4, 7, 2, 6]      #[4,1,8,3]
#[4, 7]   [2,6]       #[4,1] [8,3]
#chamando o mergesort para ordenar 
#[4]  [7]  [2]  [6]    [4]  [1]  [8]  [3]
#[2, 4, 6, 7]          [1, 3, 4, 8]
#[1, 2, 3, 4, 4, 6, 7, 8] #lista ordenada