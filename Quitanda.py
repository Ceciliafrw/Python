
def quitanda():
    global compra
    global valor_total_orc
    global fruta
        #Lista das frutas disponiveis na quitanda e indice
    quitanda_fruta = {
            "Laranja": "Laranja",
            "Melancia": "Melancia",
            "Melão": "Melão",
            "Morango": "Morango",
            }      
            #Valor das frutas de acordo com o indice das frutas
    quitanda_valor = {
            "Laranja" : 2,
            "Melancia" : 10,
            "Melão" : 5,
            "Morango" : 3,
            }
            #Quantidade das frutas de acordo com o indice das frutas
    quitanda_qnt = {
            "Laranja" : 15,
            "Melancia" : 5,
            "Melão" : 5,
            "Morango" : 25,
            }

    lista_valor_total = []
    lista_fruta = []
    lista_valor_unit = []
            #imprimindo layout de menu das frutas, quantidade e valor unitário
    print(" Fruta       Qnt Disp      Valor Unit" )
    for fruta_lista in quitanda_fruta.keys():
        print( quitanda_fruta[fruta_lista]," -   ", quitanda_qnt[fruta_lista], "     -     R$", quitanda_valor[fruta_lista], ",00")

            #criando a lista de compras do cliente
    lista_de_compras = {} 
            #identificando fruta e quantidade solicitadas pelo cliente  
    fruta = input("\n Qual fruta deseja comprar ? ").title()
    lista_fruta.append(fruta)
    Quantidade = int(input("\nQuantas {}s deseja comprar? ".format(fruta)))
    lista_de_compras[fruta] = Quantidade
            #buscando a fruta da lista para calcular valor unitário e valor total orcado pelo cliente
    for fruta_orc in lista_de_compras.keys():
           #buscando a quantidade orçado pelo cliente
        for valor_orc in lista_de_compras.values():
           
            #verificando se a fruta esta no estoque disponivel
            if fruta_orc in quitanda_valor:
           #definindo a varial de valor unitario de acordo com valor do estoque
                valor_unit = (quitanda_valor[fruta_orc])
                        #calculando o total por fruta
                valor_total_unit = (valor_unit*valor_orc)
                lista_valor_unit.append(valor_total_unit)
            #guardando o valor total por fruta (para calculo do valor total)
                lista_valor_total.append(valor_total_unit)
            #imprimindo para o cliente a fruta, valor unitario e valor total por fruta
               print("\n{} - R$  {},00 = {} ".format(fruta_orc,valor_unit,valor_total_unit))
                
                        #imprimindo o valor total do orçamento
            valor_total_orc = 0
            for valor_unit_list in lista_valor_total:
                valor_total_orc = valor_unit_list + valor_total_orc
                for frutas in lista_fruta:
                    for valor_orc in lista_valor_unit:
                        #print("{} - R$ {},00".format(frutas, valor_orc))
                        
            
                print("Total orçado = R$ {}\n".format( valor_total_orc))
                return fruta, valor_total_orc

                
def Fechando_a_venda() :
    global venda
    venda = input("Vamos fechar o orçamento?(por favor responda S/N): ").upper()
    if venda == "S":
        print("\nSua compra deu R$ {},00".format(valor_total_orc))
        print("""Temos as seguintes Formas de pagamento:
                1 - Cartão
                2 - Dinheiro
                3 - Pix""")
    forma_pgto = int(input("Qual será a forma de pagamento? (escolha o numero correspondente): "))
    if forma_pgto == 2:
        valor_pago = int(input("Valor entregue R$? "))
        troco = valor_pago - valor_total_orc
        print("Seu troco é R$ {},00\n Obrigada pela preferência {}. \n Volte Sempre".format(troco, fregues)) 
    else:
         print("Obrigada pela preferência {}. \n Volte Sempre".format(fregues)) 

            

#recepcionando e identificano o fregues
print("\nOi!Estamos muito feliz em telo em nossa quitanda hoje.\n") 
fregues = input("Qual seu nome? ").title()

print("\nOlá", fregues, "! \n   Hoje estamos com frutas fresquinhas, veja abaixo as disponibilidades: \n")
quitanda()

#definindo o loop de compra
compra = input("{} Deseja comprar mais alguma fruta? (por favor responda S/N): ".format(fregues)).upper()
while compra == "S":
    quitanda()
    lista_fruta = []
    lista_fruta.append(fruta)
    compra =  input("{} Deseja comprar mais alguma fruta? (por favor responda S/N): ".format(fregues)).upper()
    

Fechando_a_venda()
