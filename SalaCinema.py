#Montando uma sala de cinema

from ast import While
def LugaresDisponiveis():
    global poltronareservada
    poltronareservada = int(input("Selecione a poltrona desejada: "))-1

    sala[poltronareservada] = ("x")
    print(sala)

sala = []

Qntdelugares = int(input("Informe a quantidade de lugares: ") )

if Qntdelugares  == 0 :
    print("Quantidade de lugares insuficiente para iniciar uma sala")
    
else: 
    for i in range(Qntdelugares):
        sala.append(i+1) 
print(sala)
LugaresDisponiveis()

while True:
    if  Qntdelugares > len(sala):
        print("Sem poltronas disponíveis, sessão lotada.")
        
    else:
        sala[poltronareservada] = sala[poltronareservada] == ("x")
        print("Poltrona já reservada")
        LugaresDisponiveis()

