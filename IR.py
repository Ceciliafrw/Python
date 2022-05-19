#Inserçao do valor salarial para calculo do IR
salario = float(input("Digite seu Salário Bruto: "))

if(salario >= 1903.99 and salario <= 2826.65):
    salarioliq = salario * 0.925
    print("Salario com desconto de 7,5% de IR R$" ,salarioliq)
    
elif(salario >= 2826.66 and salario <=3751.05):
    salarioliq = salario * 0.85
    print("Salario com desconto de 15% de IR R$" ,salarioliq)

#De R$ 3.751,06 a R$ 4.664,68 = 22,5% de IR
elif(salario >= 3751.06 and salario <=4664.68):
    salarioliq = salario * 0.775
    print("Salario com desconto de 22,5% de IR R$" ,salarioliq)

#Maior que  R$ 4664,68 = 27,5% de IR
elif(salario >= 4664.68):
    salarioliq = salario * 0.725
    print("Salario com desconto de 15% de IR R$" ,salarioliq)

#Salario menor do que R$ 1.903,98 - Isento
else: 
    print("Salario Isento de IR R$" ,salario)
