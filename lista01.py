# Malu precisa da sua ajuda para criar um programa que verifica se uma expressão está bem formada por chaves. A definição de expressão bem formada é a seguinte:

# Uma expressão vazia é sempre bem formada (i.e. uma string vazia)
# Se E é bem formada, então { E } também é bem formada
# Se E é bem formada, então E E também é bem formada
# Ela conseguiu coletar alguns exemplos de expressões bem formadas para te ajudar a entender o problema:

# { { { } } }
# { } { }
# { { } } { }
# { { } { { } { } } }
# E também alguns exemplos de expressões mal formadas:

# { } {
# { { } } { } }
# { } { } }
# { { } } { { { } }

def main():
    leitura = input()
    percorrer_chaves = []

    #o len vai ser todos os input da leitura, pq ele vai calcular o tamanho da entrada
    # o i é a posição do elemento, ele conta a partir do zero

    for i in range(len(leitura)):
        if leitura[i] == '{':
            percorrer_chaves.append('{')
            #print(percorrer_chaves)
        if leitura[i] == '}':
            if len(percorrer_chaves) > 0:
                percorrer_chaves.pop()
                #print(percorrer_chaves)
            else:
                percorrer_chaves.append('}')
                #print(percorrer_chaves)
    if len(percorrer_chaves) == 0:
        print('S')
    else:
        print('N')
        
if __name__ == '__main__':
    main()