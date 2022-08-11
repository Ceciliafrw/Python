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

class Carta:
    naipe = ["ouros", "copas", "espadas", "paus"]
    valor = {"A": 1, 
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
  #(__gt__, __lt__, __eq__)

class Baralho:
  def embaralhar():

  def dar_carta():
  
  def devolver_carta():