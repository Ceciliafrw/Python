#Lista de Lugares

from ast import For, While
from itertools import cycle
from re import I



sala = ["A""B""C""D""E""F""G""H""I""J"]

Qntdelugares = int(input("Informe a quantidade de lugares: ") )


if Qntdelugares == 0 :
    print("Quantidade de lugares insuficiente para iniciar uma sala")

else :
    for i in range(Qntdelugares):
        sala.append(i+1) 
        itenslinha = 10
        ends = [""] * (itenslinha - 1)
        ends.append ("\n")

for sala, end in zip(range(Qntdelugares), cycle(ends)):
    print(f"{sala: >10d}", end=end)
    #print(sala)

#While (sala[] == int)
poltronareservada = int(input("Selecione a poltrona desejada: "))-1
#if sala[poltronareservada] == ("x"):
    #print("Poltrona já reservada")
    #print(Qntdelugares)
#else:
sala[poltronareservada] = ("x")

print(sala)



