class Cachorro:
    def __init__(self, nome, peso, cidade):
        self.nome = nome
        self.peso = peso
        self.cidade = cidade
        self.categoria_peso = self.classifica_peso()
    
    def classifica_peso(self):
        peso = self.peso
        if peso < 6:
            self.categoria_peso = 'pequeno'
        elif peso >= 6 and peso < 10:
            self.categoria_peso = 'medio'
        else:
            self.categoria_peso = 'grande'

nome = input("digite um nome:")
x = Cachorro(nome, 5 , 'Londres')


print(x.nome,x.peso, x.cidade)

meu_cachorro = {
    "nome" : "Bidu",
    "peso" : 5,
    "cidade" : "Londres",
    "categoria_peso": None
}

eu = {
    "nome" : "Cecilia",
    "peso" : 45,
    "cidade" : "Londres"
}


def apresenta_cachorro(cachorro):
    print(
        "Meu nome é {}, eu sou um cachorro que mora em {}".format
            (cachorro["nome"],
            cachorro["cidade"]
        )
    )

def classifica_peso(cachorro):
    peso = cachorro['peso']
    if peso < 6:
        cachorro['categoria_peso'] = 'pequeno'
    elif peso >= 6 and peso < 10:
        cachorro['categoria_peso'] = 'medio'
    else:
        cachorro['categoria_peso'] = 'grande'

    return cachorro
    

print(meu_cachorro['categoria_peso'])
apresenta_cachorro(meu_cachorro)
meu_cachorro = classifica_peso(meu_cachorro)
print(meu_cachorro['categoria_peso'])

meu_cachorro['peso'] += 10
meu_cachorro = classifica_peso(meu_cachorro)
print(meu_cachorro['categoria_peso'])



