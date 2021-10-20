# Um aluno da disciplina de Algoritmos e Estruturas de Dados resolveu praticar os algoritmos de busca que aprendeu durante as aulas. 
# Ele resolveu buscar elementos e concatenar o resultado das buscas para gerar um "STRINGÃO".

# Para isso ele resolveu usar sequências numéricas que seguem a seguinte regra: A[n+1] > A[n] para qualquer valor de n

# Dessa forma, as entradas seguiram o seguinte modelo:
# Uma sequencia de inteiros separados por espaço: A[1] A[2] A[3] ... A[x], onde x é um valor maior que 0.
# Por fim, uma sequência de inteiros separados por espaço: Q[1] Q[2] Q[3] ... Q[q], onde Q[n] é um valor qualquer.
# A saída é um "STRINGÃO" que é o resultado da concatenação de todos os valores que resultarem sucesso de todas as buscas. 
# Exemplo: Caso a sequência seja 1 2 3 4 e as buscas forem 1 3 2, os resultados das buscas serão respectivamente 1 3 2 e 
# a saída deve ser a seguinte string "132".

# Obs.: Caso a busca não seja bem sucedida, deve-se concatenar com o inteiro 0 (zero).

def rank (busca, buscaGeral):
    inicio = 0
    fim = len(busca) - 1
    while inicio <= fim:
        meio = (fim + inicio)//2
        if buscaGeral < int(busca[meio]):
            fim = meio - 1
        elif buscaGeral > int(busca[meio]):
            inicio = meio + 1
        else:
            return meio
    return inicio

def main():

    stringao = ''
    listaA = input().split()
    listaQ = input().split()
    for i in listaQ:
        item = int(i) 
        acha = rank(listaA, item)
        if acha != 0:
            stringao += i
        else:
            stringao += "0"

    print(stringao)


if __name__ == '__main__':
    main()