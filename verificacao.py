cpf_original = "145.382.206-20"
cpf_sem_validacao = 145382206
cpf_copia = cpf_sem_validacao
total = 0

#calculo do primeiro digito verificador
for peso in range(2, 11):
    digito = cpf_copia % 10 #cpf dividido por 10
    cpf_copia = cpf_copia // 10 #dividindo de maneira inteira
    resultado = digito * peso
    total = total + resultado

total_mod11 = total % 11

#calculo do segundo digito verificador
digito_ver1 = total_mod11 - total

cpf_validacao_dig1 = cpf_sem_validacao*10 + digito_ver1

cpf_copia = cpf_validacao_dig1

for peso in range(2, 12):
    digito = cpf_copia % 10 #cpf dividido por 10
    cpf_copia = cpf_copia // 10 #dividindo de maneira inteira
    resultado = digito * peso
    total = total + resultado

total_mod11 = total % 11

#calculo do primeiro digito verificador
digito_ver2 = 11 - total_mod11

cpf_Validado = cpf_validacao_dig1