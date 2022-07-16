dados = [ "nome", "logradouro", "numero", "complemento", "cep", "cidade", "estado"]
informacoes = {}

nomes = input("Por favor insira seu nome completo : ")
informacoes["nome"] = nomes

endereco = input("Por favor insira o logradouro: ")
informacoes["logradouro"] = endereco

numero = input("Por favor insira o numero da casa : ")
informacoes["numero"] = numero

complemento = input("Por favor insira um complemento : ")
informacoes["complemento"] = complemento

cep = input("Por favor informe o CEP : ")
informacoes["cep"] = cep

bairro = input("Por favor informe o bairro : ")
informacoes["bairro"] = bairro

cidade = input("Por favor informe a cidade : ")
informacoes["cidade"] = cidade

estado = input("Por favor informe o estado : ")
informacoes["estado"] = estado

   # endereco_carta = """
print("\nA entrega será em:")  
print("\n"  "Nome:", informacoes['nome'], "\n"
"Logradrouro:",informacoes['logradouro'],"nº", informacoes['numero'], informacoes['complemento'], "\n" 
"Bairro", informacoes['bairro'], "\n"
 "Cep",informacoes['cep'],"-",  informacoes['cidade'].upper(),"/", informacoes['estado'].upper(), "\n" )


   #"""
    #print(endereco_carta.format(
     #   [ "nome", "logradouro", "numero", "complemento", "cep", "cidade", "estado"]
    #))