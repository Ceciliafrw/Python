#Lista de Lugares

from ast import For
from re import I

sala = []
fileira = ["A, ""B, ""C, ""D, ""E, ""F, ""G, ""H, ""I, ""J "]

Qntdelugares = int(input("Informe a quantidade de lugares: ") )

print(fileira)

for i in range(Qntdelugares):
    sala.append(i+1) 
print(sala)

poltronareservada = int(input("Selecione a poltrona desejada: "))-1
#if sala[poltronareservada] == ("x"):
    #print("Poltrona já reservada")
    #print(Qntdelugares)
#else:
sala[poltronareservada] = ("x")

print(fileira)
print(sala)



