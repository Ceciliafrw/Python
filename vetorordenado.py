#implementar classe Vetores Ordenados
import random

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = self.capacidade*[0]    

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio.")
        else:
            for i in range(self.ultima_posicao + 1):
               print(i, "-", self.valores[i])

    def insere(self, valor):
        if self.duplicata(valor) is True:
            breakpoint
        
        else:
            
            if self.ultima_posicao == self.capacidade - 1:
                print("Capacidade máxima atingida")
                return
            posicao = 0
            for i in range(self.ultima_posicao + 1):
                posicao = i
                if self.valores[i] >= valor:
                    break
                if i == self.ultima_posicao:
                        posicao = i + 1

            x = self.ultima_posicao
            while x > posicao:
                self.valores[x + 1] = self.valores[x]
                x = x - 1
                
            self.valores[posicao] = valor
            self.ultima_posicao = self.ultima_posicao + 1

    
    def duplicata(self, valor):
        posicao = 0
        for i in range(posicao, self.ultima_posicao):
            posicao = i
            if valor == self.valores[i]:
                print(f"{i} - Valor duplicado")
                break
                
           

vetor = VetorOrdenado(8)

vetor.insere(2)
vetor.insere(3)
vetor.insere(6)
vetor.insere(7)
vetor.insere(8)
vetor.insere(9)
vetor.imprime()
print("==========")
vetor.duplicata(7)
print("==========")
vetor.imprime()
