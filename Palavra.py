
#escrever criar um dados e criar um arquivo
##nome = input("insira seu nome: ")
##with open('nome.txt', 'a') as xponteiro:
    ##xponteiro.write(nome)
    ##xponteiro.write("\n")

#ok -  Conte quantas palavras há no arquivo
#ok -  Conte quantas vezes cada letra do alfabeto aparece no arquivo
#ok -  Conte quantas palavras começam com cada letra do alfabeto
#Identifique as palavras começam com as mesmas 3 letras do seu nome e salve-as num arquivo separado
#Identifique as palavras que possuem todas as letras do seu nome e salve-as num arquivo separado
#Identifique todas as palavras que são palíndromos e salve-as num arquivo separado

#passando o nome do arquivo que deseja que seja aberto
from re import I


filename = 'todaspalavras.txt'
contar = []
#lendo um arquivo 
with open(filename,'r', encoding='utf-8') as arquivo:
    # Contando  quantas palavras há no arquivo
    for palavra in arquivo:
        contar.append(palavra.strip().upper())

#contando as palavras da lista contar
def contar_todas_palavras(contar):
#imprimindo os quantas palavras tem no arquivo
    return len(contar)

#contando quantas vezes cada letra aparece
def contar_letras_alfabeto(contar):
    dic_letras_alfabeto = {}
    for palavra in contar:
        Lista_Letras = list(palavra)
        for letra in Lista_Letras:
            if letra in dic_letras_alfabeto:
                dic_letras_alfabeto[letra] += 1
            else:
                dic_letras_alfabeto[letra] = 1
    return dic_letras_alfabeto

#contando as letra iniciais
def contar_letras_inicio(contar):
    dic_letras_inicial= {}
    for palavra in contar:
        if palavra[0] in dic_letras_inicial:
                dic_letras_inicial[palavra[0]] += 1
        else:
                dic_letras_inicial[palavra[0]] = 1
    return dic_letras_inicial

#contando quantas palavras tem a inicial do meu nome
def contar_letras_meu_nome(contar):
    dic_letras_inicial_meu_nome= {"CEC" : 0}
    for palavra in contar:
        if palavra[0] in dic_letras_inicial_meu_nome:
                dic_letras_inicial_meu_nome[palavra[0]] += 1

    return dic_letras_inicial_meu_nome

#imprimindo os resultados
qnt_palavras = contar_todas_palavras(contar)
qnt_letras = contar_letras_alfabeto(contar)
qnt_letras_inicial_meu_nome = contar_letras_meu_nome(contar)
qnt_letras_inicial = contar_letras_inicio(contar)
print("Eu consegui contar as", qnt_palavras , "palavras via Python\n")
print("As letras do meu nome aparecem:", qnt_letras_inicial_meu_nome)
print("A quantidade de cada letras é:\n")
for letra in qnt_letras:
    print(letra, ":",qnt_letras[letra])

print("O acumulado de letras é:\n")
for letra in qnt_letras_inicial:
    print(letra, ":",qnt_letras_inicial[letra])


    