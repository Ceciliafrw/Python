
#escrever criar um dados e criar um arquivo
##nome = input("insira seu nome: ")
##with open('nome.txt', 'a') as xponteiro:
    ##xponteiro.write(nome)
    ##xponteiro.write("\n")

#ok - Conte quantas palavras há no arquivo
#ok - Conte quantas vezes cada letra do alfabeto aparece no arquivo
#ok - Conte quantas palavras começam com cada letra do alfabeto
#ok - Identifique as palavras começam com as mesmas 3 letras do seu nome e salve-as num arquivo separado
#ok - Identifique as palavras que possuem todas as letras do seu nome e salve-as num arquivo separado
#ok - Identifique todas as palavras que são palíndromos e salve-as num arquivo separado

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


def contar_letras_inicio(contar):
    dic_letras_inicial= {}
    for palavra in contar:
        if palavra[0] in dic_letras_inicial:
                dic_letras_inicial[palavra[0]] += 1
        else:
                dic_letras_inicial[palavra[0]] = 1
    return dic_letras_inicial


def contar_letras_inicio_meu_nome(contar, iniciais):
    with open('Iniciais Meu nome.txt', 'a') as meu_arquivo:
         for palavra in contar:
            if palavra[:3] == iniciais:
                meu_arquivo.write(palavra)

def contar_letras_meu_nome(contar):
    meu_nome = ['C','E','L','I','A']
    with open('Meu nome completo.txt', 'a') as arquivo_nome:
        for letra in meu_nome:
            for palavra in contar:
                if palavra[0] == letra:
                    arquivo_nome.write(palavra)
                    arquivo_nome.write("\n")

def palavra_palindromo(contar):
     with open("palavras_palindromos.txt", "w") as arquivo_palindromo:
        for palavra in contar:
            if palavra.strip() == palavra.strip()[::-1]:
                arquivo_palindromo.write(palavra)
                arquivo_palindromo.write("\n")


#imprimindo os resultados
contar_letras_inicio_meu_nome(contar, iniciais="CEC")
contar_letras_meu_nome(contar)
palavra_palindromo(contar)
qnt_palavras = contar_todas_palavras(contar)
qnt_letras = contar_letras_alfabeto(contar)
qnt_letras_inicial = contar_letras_inicio(contar)
print("Eu consegui contar as", qnt_palavras , "palavras via Python\n")
print("\nA quantidade de cada letras é:\n")
for letra in qnt_letras:
    print(letra, ":",qnt_letras[letra])

print("\nO acumulado de letras é:\n")
for letra in qnt_letras_inicial:
    print(letra, ":",qnt_letras_inicial[letra])


    