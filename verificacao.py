
from contextlib import nullcontext
from unicodedata import numeric

def solicita_cpf():
    cpf_usuario = input("Digite seu CPF: ")

    cpf_usuario_tratado = ''
    for char in cpf_usuario:
        if char.isnumeric():
            cpf_usuario_tratado = cpf_usuario_tratado + char
 
    return cpf_usuario_tratado

if __name__ == '__main__':

    cpf_usuario_tratado = solicita_cpf()
    cpf_original =cpf_usuario_tratado[:9] #pegando os 9 primeiros digistos
    cpf_sem_validacao = int(cpf_original)
    cpf_copia = cpf_sem_validacao
    total = 0

    #calculo do primeiro digito verificador
    for peso in range(2, 11): #extraindo numero a direita
        digito = cpf_copia % 10 #cpf dividido por 10
        cpf_copia = cpf_copia // 10 #dividindo de maneira inteira para excluir o ultimo digito

        resultado = digito * peso
        total = total + resultado

    total_mod11 = total % 11
    digito_ver1 = 11 - total_mod11
    if digito_ver1 >= 10:
        digito_ver1 = 0
    print(f"O primeiro digito verificador é {digito_ver1}")

    cpf_validacao_dig1 = cpf_sem_validacao*10 + digito_ver1 
    #calculo do segundo digito verif
    cpf_copia = cpf_validacao_dig1 

    total = 0
    for peso in range(2, 12): #avançar 11 casas
        digito = cpf_copia % 10 #cpf dividido por 10
        cpf_copia = cpf_copia // 10 #dividindo de maneira inteira
        resultado = digito * peso
        total = total + resultado

    total_mod11 = total % 11
    digito_ver2 = 11 - total_mod11
    if digito_ver2 >= 10:
        digito_ver2 = 0
    print(f"O segundo digito verificador é {digito_ver2}")

    cpf_validado = cpf_validacao_dig1*10 + digito_ver2 
    print(f"O cpf validado é {cpf_validado}")

    cpf_validado_str = str(cpf_validado)
    if len(cpf_validado_str) < 11:
        zeros_qtd = 11 - len(cpf_validado_str)
        for i in range(zeros_qtd):
            cpf_validado_str = '0' + cpf_validado_str
            print(f"O cpf validado é {cpf_validado_str}")

    if cpf_validado_str == cpf_usuario_tratado:
        print("Este CPF é valido")

    else:
        print("Esté CPF é Inválido!!")


