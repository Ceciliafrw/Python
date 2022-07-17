from ast import While
from itertools import count
#definindo quantos itens por linha
def split_list(lst,l):
    for n in range(0, len(lst), l):
        yield lst[n:n + l]

l = 7

#desenhando a pista e excluindo as jogadas
def Pinos_Disponiveis():
    global pinos
    
    lista = []
    print("Sua pista de boliche tem de 0 a 34 possiveis jogadas")
    # Concorda que é um pouco estranho ter 10 pinos, mas 34 possíveis jogadas?
    # O que daria pra fazer é oferecer apenas 10 jogadas, que correspondem aos 10 pinos. Aí ali embaixo você adapta a lógica
    valores = input("Quais pinos quer derrubar (separe por virgula (',')): ")
    lista = valores.split(",") # Sensacional o uso desse split, parabéns! Ótima ideia!
    #print(totallugares)
    for pino in lista:  # tente usar variáveis com nomes esclarecedores
        if pino  not in listajogada:
            # No lugar desse if você poderia fazer assim
            posicao = posicao_dos_pinos[pino]  # Isso vai te dar o index de onde está o pino "x" dentro da lista que corresponde à pista
            pinos[posicao] = " "  # Isso derruba apenas a posição do pino
            # O seu código estava quase 100%. O problema é que ó jogador poderia alterar outras partes da pista que não são pinos.
            # Por exemplo, experimente derrubar a posicao 9 no código anterior... A pista fica desalinhada

#imprimindo a pista com os pinos em forma triangular
def Pista():
    global pino
    for pino in pinos:
        print(pino, end="")


contador = 0
#pinos
pinos = [" ","9"," ","9"," ","9"," ","9"," ","\n ",
" ", "9"," ","9"," ","9"," "," "," ","\n ",
" "," ","9"," ","9"," "," "," "," "," ","\n"    
" "," "," "," ","9"," "," "," "," "," "," "," ","\n"]

#numero da posição dos pinos na pista
posicao_dos_pinos = {
'1' : 1, '6' : 13, # Há dois pinos 5
'2' : 3, '7' : 15,
'3' : 5, '8' : 22,
'4' : 7, '9' : 24,
'5' : 11, '10' :34,
}

#lista de jogadas já efetuadas
listajogada = []

#loop para verificar enquanto tem pinos disponiveis para a jogada
while True:
    if "9" in pinos:
        Pista()
        Pinos_Disponiveis()
        contador = contador + 1 # Muito boa a ideia de contar jogadas!
    else:
        print("\n\nJogo encerrado")
        print(f"Voce fez {contador} jogadas")
        break

