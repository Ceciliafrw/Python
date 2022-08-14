#Criar uma classe chamada "MarvelViloes" onde terão os atributos nome(str), poderes(list), perigo(int).
#- A classe deve conter os métodos Getters e Setters de cada atributo. (Exemplo: def get_nome, def set_nome)
#- O atributo perigo deve receber valores somente entre 0 a 5.
#- A classe MarvelViloes deve conter um método chamado "dominar_mundo()".
#- "dominar_mundo()" deve realizar uma validação do perigo do vilão com as seguintes condicionais:
#- Para perigo de menor ou igual a 2 retornar "Vilão Morto"
#- Para perigo maior que 2 e menor que 5 retornar "Vilão Preso"
#- Para perigo igual a 5 retornar "Vilão Dominou o Mundo"

class MarvelViloes():
    def __init__ (self, vilao, poderes, perigo):
        self.vilao = vilao
        self.poderes = poderes
        self.perigo = perigo
        
        print(f"{vilao} tem o poder {poderes} seu poder é perigoso nível {perigo}")
    
    def dominar_mundo(self, perigo):
        if perigo <= 2:
            print("Vilão Morto")
        
        elif perigo == 2 or perigo <= 5:
            print("Vilão Preso")
        
        else:
            print("Vilão Dominou o Mundo")

    def get_vilao(self):
        return self.vilao

    def get_poderes(self):
        return self.poderes

    def get_perigo(self):
        return self.perigo

    def set_vilao(self, vilao):
        self.vilao = vilao

    def set_poderes(self, poderes):
        self.poderes = poderes
    
    def set_perigo(self, perigo):
         self.perigo = perigo

marvel = MarvelViloes("Cecilia", "Le pensamento", 5)

vilao = input("\nQual nome do seu vilão? ")
poderes = input("Qual poder do seu vilão? ")
perigo = int(input("Quão perigoso é o seu vilão de 0 a 5? "))

marvel.set_vilao(vilao)
marvel.set_poderes(poderes)
marvel.set_perigo(perigo)

print("{} tem o poder de {} é perigoso no nivel {}".format(marvel.get_vilao(),marvel.get_poderes(),marvel.get_perigo()))
marvel.dominar_mundo(perigo)