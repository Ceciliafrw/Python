#implementar linha encadeada

from wsgiref.validate import validator


class Noh:
    def __init__(self, valor ):
        self.valor = valor
        self.proximo = None

    def mostra_noh(self):
        print(self.valor)

    def mostra_proximo(self):
        print(self.proximo)

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def insere_inicio(self, valor):
        novo = Noh(valor)
        novo.proximo = self.head
        self.head = novo

    def exclui_inicio(self):
        temp = None
        if self.head != None:
            temp = self.head.valor
            self.head = (self.head).proximo #olhando pro primeiro valor
        else: 
            print("Lista vazia")

        return temp
    
    def excluir_posicao(self, valor): #excluir atual
        atual = self.head 
        anterior = None
        while atual != None:
            if atual.valor == valor:
                anterior = atual.proximo            
            else:
                anterior = atual.proximo
            atual = atual.proximo



    def mostrar(self): # imprimindo os local
        atual = self.head
        while atual != None:
            atual.mostra_noh()
            atual = atual.proximo


"""
print("Noh 1")
noh_1 = Noh(5)
noh_1.mostra_noh()
noh_1.mostra_proximo()

print("\nNoh 2")
noh_2 = Noh(42)
noh_2.proximo = noh_1 # mostra onde esta salvo o no 1
noh_2.mostra_noh()
noh_2.mostra_proximo()

(noh_2.proximo).mostra_noh() # mostra o valor do no1
"""

lista = ListaEncadeada()
lista.insere_inicio(4)
lista.insere_inicio(7)
lista.insere_inicio(9)
lista.insere_inicio(42)
lista.insere_inicio(13)
lista.insere_inicio(22)
lista.mostrar()

print("==================")
for i in range(4):
    print("pop = {}". format(lista.exclui_inicio()))
lista.exclui_inicio()
lista.mostrar()

print("==================")
lista.exclui_inicio()
lista.mostrar()