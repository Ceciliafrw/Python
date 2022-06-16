from ast import While
from itertools import count
def split_list(lst,l):
    for n in range(0, len(lst), l):
        yield lst[n:n + l]

l = 7

def Pinos_Disponiveis():
    global pinos
    jogada = int(input("Quais pinos quer derrubar: "))
    #print(totallugares)
    pinos.pop(jogada)
 
    return

def Pista():
    global pino
    for pino in pinos:
        print(pino, end="")


pinos = [" ","I"," ","I"," ","I"," ","I"," ","\n ",
" ", "I"," ","I"," ","I"," "," "," ","\n ",
" "," ","I"," ","I"," "," "," "," "," ","\n"    
" "," "," "," ","I"," "," "," "," "," "," "," ","\n"]

posicao_dos_pinos = {
'1' : 1, '5' : 13,
'2' : 3, '6' : 15,
'3' : 5, '7' : 22,
'4' : 7, '8' : 24,
'5' : 11, '10' :34,
}

#print(pinos)
while True:
    if "I" in pinos:
        Pista()
        Pinos_Disponiveis()
    else:
        print("Jogo encerrado")