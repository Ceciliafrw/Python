
#escrever criar um dados e criar um arquivo
##nome = input("insira seu nome: ")
##with open('nome.txt', 'a') as xponteiro:
    ##xponteiro.write(nome)
    ##xponteiro.write("\n")


#passando o nome do arquivo que deseja que seja aberto
filename = 'todaspalavras.txt'
contar = []
#lendo um arquivo
with open(filename,'r', encoding='utf-8') as arquivo:
    #imprimindo os dados do arquivo
    for palavra in arquivo:
        contar.append(palavra.strip())

print("Eu consegui contar as", len(contar), "palavras via Python")

    if palavra  "C":
        palavra.append(palavra.strip())