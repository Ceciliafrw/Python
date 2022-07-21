
#escrever criar um dados e criar um arquivo
##nome = input("insira seu nome: ")
##with open('nome.txt', 'a') as xponteiro:
    ##xponteiro.write(nome)
    ##xponteiro.write("\n")

#ok - Conte quantas palavras há no arquivo
#Conte quantas vezes cada letra do alfabeto aparece no arquivo
#Conte quantas palavras começam com cada letra do alfabeto
#Identifique as palavras começam com as mesmas 3 letras do seu nome e salve-as num arquivo separado
#Identifique as palavras que possuem todas as letras do seu nome e salve-as num arquivo separado
#Identifique todas as palavras que são palíndromos e salve-as num arquivo separado

#passando o nome do arquivo que deseja que seja aberto
from re import I


filename = 'todaspalavras.txt'
contar = []
#lendo um arquivo
with open(filename,'r', encoding='utf-8') as arquivo:
    #imprimindo os dados do arquivo
    for palavra in arquivo:
        contar.append(palavra.strip())

print("Eu consegui contar as", len(contar), "palavras via Python")

#for palavra in contar:
    #letra_inicial = re.findall(r'\b(c[a,z]\b', text, re.I)
    #print(letra_inicial)