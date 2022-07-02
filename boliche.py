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
    valores = input("Quais pinos quer derrubar (separe por virgula (',')): ")
    lista = valores.split(",")
    #print(totallugares)
    for y in lista:
        x = int(y)
        if x  not in listajogada:
            if(x >= 0 and x <= 34):
                pinos[x] = " "

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
'1' : 1, '5' : 13,
'2' : 3, '6' : 15,
'3' : 5, '7' : 22,
'4' : 7, '8' : 24,
'5' : 11, '10' :34,
}

#lista de jogadas já efetuadas
listajogada = []

#loop para verificar enquanto tem pinos disponiveis para a jogada
while True:
    if "9" in pinos:
        Pista()
        Pinos_Disponiveis()
        contador = contador + 1 
    else:
        print("\n\nJogo encerrado")
        print(f"Voce fez {contador} jogadas")
        break

