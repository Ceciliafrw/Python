from random import randint

def valida_jogador(jogador):
    if jogador.isnumeric():
        jogador = int(jogador)
                
    else:
        jogador = input("Digite um valor numérico: ")
        jogador = int(jogador)
      

    return jogador

def Jogo_Par_Impar():
    while True:    
        jogador = input("Digite um valor: ")
        jogador_validado = valida_jogador(jogador)
        computador = randint(0,5)
        total = jogador_validado  + computador
        tipo = str(input("Escolha Par ou Ímpar (P/I): ")).strip().upper()[0]
        par_impar(tipo)
        print(f"Você jogou {jogador_validado} e o computador jogou {computador} total {total}")
        ganhador(total, tipo)
        
        return total, tipo

def par_impar(tipo):
    
    while tipo not in "PI":
        total = Jogo_Par_Impar()
        if total % 2 == 0:
            tipo = "P"
            print("Deu par")
        else:
            print("Deu Ímpar")
            tipo = "I"
        
        return tipo
   
def ganhador(total, tipo):
    vitoria = 0
    if tipo == "P":
        if total % 2 == 0:
            print("Você Ganhou!")
            vitoria += 1
        else:
            print("Você Perdeu!")
            breakpoint

    elif tipo == "I":
        if total % 2 == 1:
            print("Você Ganhou!")
            vitoria += 1
        else:
            print("Você Perdeu!")
            breakpoint

        print("Vamos jogar denovo!")
    print(f"GAME OVER! Você venceu {vitoria} vezes")

#contador = 0
#while contador == 5:
Jogo_Par_Impar()
    #contador += 1
