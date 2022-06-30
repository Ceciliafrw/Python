# Atenção com esses imports desnecessários. É coisa do VS Code, mas é bom sempre estar esperto

def Pinos_Disponiveis():
    # Aqui eu entendo que a variável "pinos" é a mesma lá de baixo, por isso usaste o "global"
    global pinos
    jogada = int(input("Quais pinos quer derrubar: "))
    #print(totallugares)
    # Nessa linha que há um problema... 
    # O método pop remove um elemento de lista. 
    # Mais especificamente, se você chamar lista.pop(numero) o que vai acontecer é que o elemento que estiver no index "numero" será removido.
    # Por isso seu código não funciona, porque a cada jogada um elemento da lista é removido. Faça um teste e rode seu código passando o número 5 várias vezes
    pinos.pop(jogada)
    # O correto seria você não remover elementos, mas alterá-los. As etapas seriam essas:
    #  - 1: Solicitar um pino ao usuário (ok)
    #  - 2: Descobrir em qual posição da lista pinos ele se encontra (use o dicionário lá de baixo para isso)
    #  - 3: Substitua o pino por outro caractere (equivale a fazer algo parecido com isso pinos[jogada] = '_' )
 
    return

def Pista():
    # Note que essa variável "pino" não é usada em mais lugar nenhum, por isso não há necessidade de usar a palavra "global"
    # global pino
    for pino in pinos:
        print(pino, end="")


pinos = [" ","I"," ","I"," ","I"," ","I"," ","\n ",
" ", "I"," ","I"," ","I"," "," "," ","\n ",
" "," ","I"," ","I"," "," "," "," "," ","\n"    
" "," "," "," ","I"," "," "," "," "," "," "," ","\n"]

posicao_dos_pinos = {
'1' : 1, '5' : 13,
'2' : 3, '6' : 15,
'3' : 5, '7' : 22,
'4' : 7, '8' : 24,
'5' : 11, '10' :34,
}

#print(pinos)
while True:
    # Gostei que você usou essa expressão "if 'I' in pinos", achei muito bom!!
    if "I" in pinos:
        Pista()
        Pinos_Disponiveis()
    else:
        # Note que o while true continua mesmo quando o jogo acaba. O que faltou aqui é um break
        print("Jogo encerrado")