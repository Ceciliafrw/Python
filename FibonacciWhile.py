Qnt = 1

while (Qnt > 0):
#Quantidade de vezes que vai rodar Fibonacci
    Qnt = int(input("Digite a quantidade de vezes para calculo do Fibonacci : "))

#contar as vezes que rodou
    contador = 1

    #variaveis inicial para calcular fibonacci
    Primeironum = 0
    Segundonum = 1

    #imprimir as primeiras variaveis
        
        #print( Segundonum )
    print( Primeironum )
        #calcular o fibonacci
    while (contador < Qnt):
        
        Soma = Primeironum + Segundonum
        Primeironum = Segundonum
        Segundonum = Soma
        print(Soma)
        contador += 1


