#Quantidade de vezes que vai rodar Fibonacci
Qnt = int(input("Digite a quantidade de vezes para calculo do Fibonacci : "))

#contar as vezes
contador = 0

#variaveis inicial
x = 0
y = 1

print(x)
#print(y)

while (contador < Qnt):
    x = y + x
    print(x)
    contador += 1

