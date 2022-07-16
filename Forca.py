#ocultando a palavra
from getpass import getpass

#brincando de forca
palavra_inicial =  getpass("Informe uma palavra para a forca: ")
chances = 6
erros = 0
finalizei = False
letras_usadas = []
#verificando se a palvra informada é alphabetica e valida
is_valida = palavra_inicial.isalpha()
if not is_valida:
    print("Esssa palavra não é valida.")
    exit()

palavra_inicial = palavra_inicial.strip().upper()

#imprimindo o desenho da força ou as palavras
while erros < chances and not finalizei:
    for letra in palavra_inicial:
        if letra in letras_usadas:
            print(letra, end=' ')
        else:
            print("_", end=' ')
    print()

 
    #solicitando palpite do usuario
    palpite = input("Informe uma letra: ").upper()
    palpite_valido = palpite.isalpha() and len(palpite)==1

    while not palpite_valido:
        palpite = input("Seu palpiete foi invalido. Informe uma letra: ").upper()
        palpite_valido = palpite.isalpha() and len(palpite)==1

    palpite = palpite.upper()

    #verificando se letra foi usada
    if palpite in letras_usadas:
        print("Essa letra ja foi usada")
    else:
        letras_usadas.append(palpite)

    #verificando se a letra esta no palpite inicial
    if palpite in palavra_inicial:

       #verificar se finalizamos o jogo
        pontos = 0 
        for letra in palavra_inicial:
            if letra in letras_usadas:
                pontos += 1
        if pontos == len(palavra_inicial):
            finalizei = True
            
    else:
        erros = erros + 1
        
        
    print("Erros permitidos", chances - erros)

    if finalizei == True:
        print("\n Palavra: ",palavra_inicial)
        print("\nParabéns!! Você ganhou..")
    