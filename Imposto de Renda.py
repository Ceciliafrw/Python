#Inserçao do valor salarial para calculo do IR
salario = float(input("Digite seu Salário: "))


#calculo do IR de acordo com a faixa salarial
#De R$ 1.903,99 a R$ 2.826,65 = 7,5% de IR
If salario >= 1903.99 and <= 2826.65
    salarioliq = salario * 92.doc5
    Print ("Salario com desconto de 7,5% de IR " ,salarioliq)

#De R$ 2.826,66 a R$ 3.751,05 = 15% de IR
    elif salario >= 2826.66 and  <=3751.05
    salarioliq = salario * 85
    Print ("Salario com desconto de 15% de IR " ,salarioliq)

#De R$ 3.751,06 a R$ 4.664,68 = 22,5% de IR
    elif salario >= 3751.06 and  <=4664.68
    salarioliq = salario * 77.5
    Print ("Salario com desconto de 22,5% de IR " ,salarioliq)

#Maior que  R$ 4664,68 = 27,5% de IR
    elif salario >= 4664.68
    salarioliq = salario * 72.5
    Print ("Salario com desconto de 15% de IR " ,salarioliq)

#Salario menor do que R$ 1.903,98 - Isento
else 
print ("Salario Isento de IR")


