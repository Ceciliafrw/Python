#implementar pilha
from wsgiref.validate import validator


class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = self.capacidade*[0]
    
    def imprime(self):
        if self.topo == -1:
            print("A pilha está vazio.")
        else:
            for i in range(self.topo, -1, -1):
               print(i, "-", self.valores[i])

    def empilhar(self, valor):
        if self.topo == self.capacidade - 1:        #verifica  se esta cheia a lista
            print("Pilha esta cheia")
        else:
            self.topo +=1
            self.valores[self.topo] = valor

    def desimpilhar(self):
        if self.topo == -1:
            print("A pilha está vazio.")
        else:
            valor_temporario = self.valores[self.topo]
            self.topo -=1
            return valor_temporario


vetor = Pilha(8)

vetor.empilhar(4)
vetor.empilhar(7)
vetor.empilhar(1)
vetor.empilhar(2)
vetor.empilhar(5)
vetor.empilhar(4)
vetor.empilhar(12)
vetor.empilhar(6)

vetor.imprime()

print("==========")
print("Tirei o valor {}".format(vetor.desimpilhar()))