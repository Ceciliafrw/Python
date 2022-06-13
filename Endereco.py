dados = [ "nome", "logradouro", "numero", "complemento", "cep", "cidade", "estado"]
informacoes = {}

for dado in dados:
    pergunta = "Por favor insira " + dado + ":"
    informacoes = pergunta

    endereco_carta = """
    {}
    {}, {} - {}
    {}, {}/{}
    {}



s
    """
    print(endereco_carta.format(
        
        [ "nome", "logradouro", "numero", "complemento", "cep", "cidade", "estado"]
    ))