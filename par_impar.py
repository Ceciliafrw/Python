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
        tipo_p = par_impar()
        print(f"Você jogou {jogador_validado} e o computador jogou {computador} total {total}")
        ganhador(total, tipo_p)
        return total

def par_impar():
    tipo = str(input("Escolha Par ou Ímpar (P/I): ")).strip().upper()[0]
    while tipo not in "PI":
        total = Jogo_Par_Impar()
        if total % 2 == 0:
            tipo = print("Deu Par")
        else:
            tipo = print("Deu Ímpar")
        
        return tipo
   
def ganhador(total, tipo):
    vitoria = 0
    tipo = par_impar(tipo)

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


Jogo_Par_Impar()