
quitanda_fruta = {
    1: "Laranja ",
    2: "Melancia",
    3: "Melão   ",
    4: "Morango ",
}

quitanda_valor = {
    1 :  1,
    2 : 10,
    3 :  5,
    4 :  2,
}

quitanda_qnt = {
    1 : 15,
    2 :  5,
    3 :  5,
    4 : 25,
}

print("Oi!Estamos muito feliz em telo em nossa quitanda hoje.\n") 
fregues = input("Qual seu nome? ")

print("\n Olá", fregues, "! \n   Hoje estamos com frutas fresquinhas, veja abaixo as disponibilidades: \n")
print(" Fruta       Qnt Disp      Valor Unit" )
for num in quitanda_fruta:
    print( quitanda_fruta[num]," -   ", quitanda_qnt[num], "     -     R$", quitanda_valor[num], ",00")


#print("\n E qual seu pedido para hoje? Temos:", nome)
#fruta = title(input("Qual fruta gostaria de comprar?"))
#qnt_fruta =input("Hoje estamos com um estoque de: ", quitanda_qnt(quitanda_fruta), quitanda_valor(quitanda_fruta) )
