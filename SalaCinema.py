#Montando uma sala de cinema

from itertools import count


def split_list(lst,l):
    for n in range(0, len(lst), l):
        yield lst[n:n + l]

l = 10

def LugaresDisponiveis():
    global poltronareservada
    global totallugares
    poltronareservada = int(input("\nSelecione a poltrona desejada: "))-1
    #print(totallugares)

    if sala[poltronareservada] != ("0"):
        sala[poltronareservada] = ("0")
        totallugares = int(totallugares) - 1
        print("Poltrona" ,poltronareservada+1, "reservada\n")

    elif totallugares == (0):
        print("\nSem poltronas disponíveis, sessão lotada.\n")
    
    else:
        print("\nPoltrona reservada, escolha outra \n")

    return

def cinema():
    global fileiras
    global coluna
    fileira = list(split_list(sala, l))
    print(coluna)
    for fileiras in fileira:
        print(fileiras)
    
sala = []
coluna = ["A  B  C  D  E  F  G  H  I  J "]

Qntdelugares = int(input("Informe a quantidade de lugares: ") )

while (Qntdelugares) == 0 :
    print("Quantidade de lugares insuficiente para iniciar uma sala - REINICIE A SESSÃO")
    Qntdelugares = int(input("Informe a quantidade de lugares: ") )

else:

    for i in range(Qntdelugares):
            sala.append(i+1)
            totallugares = len(sala)

    while (totallugares) >= 0 :
        cinema()
        LugaresDisponiveis()
        if  totallugares == (0):
            print("\nSem poltronas disponíveis, sessão lotada.\n")
            cinema()
            print("O Filme já vai começar\n")
            break


        