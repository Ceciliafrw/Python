
#escrever criar um dados e criar um arquivo
##nome = input("insira seu nome: ")
##with open('nome.txt', 'a') as xponteiro:
    ##xponteiro.write(nome)
    ##xponteiro.write("\n")


#passando o nome do arquivo que deseja que seja aberto
filename = 'nome.txt'
#lendo um arquivo
with open(filename,'r') as xponteiro:
    #imprimindo os dados do arquivo
    for linha in xponteiro:
        #strip para eliminar o \n ao imprimir
        print(linha.strip())