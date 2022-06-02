sala = []
fileira = ["A, ""B, ""C, ""D, ""E, ""F, ""G, ""H, ""I, ""J "]

Qntdelugares = int(input("Informe a quantidade de lugares: ") )

print(fileira)

for i in range(Qntdelugares):
    sala.append(i+1) 
print(sala)

poltronareservada = int(input("Selecione a poltrona desejada: "))-1

sala[poltronareservada] = ("x")

print(fileira)
print(sala)