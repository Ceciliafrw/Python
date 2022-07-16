
#escrever criar um dados e criar um arquivo
##nome = input("insira seu nome: ")
##with open('nome.txt', 'a') as xponteiro:
    ##xponteiro.write(nome)
    ##xponteiro.write("\n")


#passando o nome do arquivo que deseja que seja aberto
filename = 'todaspalavras.txt'
#lendo um arquivo
with open(filename,'r', encoding='utf-8') as xponteiro:
    #imprimindo os dados do arquivo
    for linha in xponteiro:
        todaspalavras.append(linha.strip())
        #strip para eliminar o \n ao imprimir
        print(len(todaspalavras))