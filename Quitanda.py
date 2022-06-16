from turtle import title

#listando as frutas e o numero de estoque
quitanda_fruta = {
    1: "Laranja",
    2: "Melancia",
    3: "Melão",
    4: "Morango",
}
indice_frutas = quitanda_fruta.items()

#listando valor por fruta
quitanda_valor = {
    "Laranja" : 0.50,
    "Melancia" : 10,
    "Melão" : 5,
    "Morango" : 0.25,
}
indice_valor = quitanda_valor.items()

#listando estoque de frutas
quitanda_qnt = {
    "Laranja" : 15,
    "Melancia" : 5,
    "Melão" : 5,
    "Morango" : 25,
}
indice_qnt = quitanda_qnt.items()


#print("Oi freguês!! \n Estou muito feliz em telo em nossa quitanda hoje.") 
#print("\n E qual seu pedido para hoje? Temos as opções abaixo:")
for indice, fruta in indice_frutas:
    print(indice, fruta, quitanda_qnt(fruta),quitanda_valor(fruta))
  #for f, valor in indice_valor:
      #for fr, qnt in indice_qnt:

          
#fruta = input("Qual fruta gostaria de comprar?")
#qnt_fruta =input("Hoje estamos com um estoque de: ", quitanda_qnt(quitanda_fruta), quitanda_valor(quitanda_fruta) )
