#Crie uma classe Carta. Ela deve ter:
#Um naipe (ouros, copas, espadas ou paus) e um valor (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, Q, J ,K)
#Um método de validação que verifique se o naipe e o valor da carta estão entre as opções permitidas
#Um método que permita imprimir diretamente a identidade da carta (naipe + valor)
#Métodos de comparação (__gt__, __lt__, __eq__) entre cartas. Considere que:
  #- Uma carta é maior que outra se seu valor for maior. Considere que A vale 1, Q vale 11, J vale 12 e o K , 13. 
  #- O naipe não influencia no valor das cartas
#Crie uma classe Baralho. Ela deve ter:
#Um atributo chamado cartas, que é uma lista com todas as cartas de um baralho comum. Inicialize essa lista dentro do método __init__ utilizando a classe Carta para criar as cartas
#Um método embaralhar, que embaralha a ordem da lista cartas (para isso talvez você queira voltar pacote random e dar uma procurada. Lembre que embaralhar em inglês é shuffle)
#Um método dar_carta, que retorna a última carta da lista cartas. Essa carta deve ser removida do baralho durante a execução desse método
#Um método devolver_carta, que recebe uma Carta como entrada e a insere novamente na lista cartas em uma posição aleatória
from ast import Import
import random

class Carta:
    __naipe = ["ouros", "copas", "espadas", "paus"]
    __naipes_unicode = {
                        "ouros"   :"\u2666",
                        "copas"   :"\u2665", 
                        "espadas" :"\u2660",
                        "paus"    :"\u2663"
                        }
    __carta = ["A","2","3","4","5","6","7","8","9","10","Q","J","K"]
    __valor_carta = {"A": 1, 
             "2": 2, 
             "3": 3, 
             "4": 4, 
             "5": 5,
             "6": 6, 
             "7": 7, 
             "8": 8, 
             "9": 9,
            "10": 10, 
             "Q": 11,
             "J": 12 ,
             "K": 13 }
 
    def __init__(self, naipe, valor):
      #self.valida_carta(naipe, valor)
      self.naipe = naipe
      self.valor = valor

    def valida_carta(self):
      
      if self.valor not in self.__valor_carta: 
        print("Valor não é de uma carta.")
        breakpoint

        if self.naipe not in self.__naipe:
          print("Valor não é de um naipe.")
          breakpoint

        return True
    
    def mostrar(self): 
        if self.valida_carta() is True:
          breakpoint

        else:
          naipe_unicode = self.__naipes_unicode[self.naipe]
          print(f"{naipe_unicode}\n{self.valor} ")

class Baralho:
  Carta = Carta("A","ouros")
  def __init__(self):
    naipe_unicode = Carta.__naipes_unicode
    cartas = Carta.__carta
    for naipe in naipe_unicode:
      for valor in cartas:
        print(f"{naipe}\n{valor} ")


  #def embaralhar(self.Carta):

  def dar_carta():
    naipe = random.choice(Carta.__naipes_unicode)
    carta = random.choice(Carta.__carta)
    print(naipe, carta)

  #   def devolver_carta():

#carta = Carta("copas", "B")
#carta.mostrar()

Baralho.dar_carta()