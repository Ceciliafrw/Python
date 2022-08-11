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
    
    def dominar_mundo():