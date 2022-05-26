#Quantidade de vezes que vai rodar Fibonacci
from ast import For


Qnt = int(input("Digite a quantidade de vezes para calculo do Fibonacci : "))

#variaveis inicial
Primeironum = 0
Segundonum = 1

#imprimindo primeiros numeros
print(Primeironum)
print(Segundonum)

#rodando o loop para calcular o fibonacci
for Num in range (Qnt):
    Soma = Primeironum + Segundonum
    print(Soma) 
    Primeironum = Segundonum
    Segundonum = Soma




 