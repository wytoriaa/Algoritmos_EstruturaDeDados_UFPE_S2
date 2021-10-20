#Dadas N listas com elementos separados por ,, imprima a maior delas.
#Seguem N linhas, cada uma contendo uma lista de elementos separados por , e delimitada por [ e ].
#Importe System.IO para detectar o fim da entrada.
#Imprima a maior das N listas, como dada na entrada.
#Em caso de empate, deve-se imprimir a primeira das N listas que possui tal maior número de elementos.

import sys
def main():
    largura = ''
    comprimento = -1
    for line in sys.stdin:
        line = line[:-1]
        quantidade = line.count('{,}')
        if line != '[]':
            quantidade = quantidade + 1
        if quantidade > comprimento:
            largura = line
            comprimento = quantidade
    print(largura)


if __name__ == '__main__':
    main()
