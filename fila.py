#implementar uma filial circular
class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.num_elementos = 0
        self.valores = self.capacidade*[0]
    
    def imprime(self):
        if self.final == -1:
            print("A fila está vazia.")
        else:
            for i in range(self.inicio, self.final + 1):
               print(i, "-", self.valores[i])

    def enfileirar(self, valor):
        # self.final += 1
        # self.valores[self.final] = valor
        
        if (self.final == self.inicio - 1) and self.final == self.capacidade - 1:        #verifica  se esta cheia a lista
            print("Fila esta cheia")
        else:
            if self.final == self.capacidade - 1:
                self.final = 0
            else:
                self.final +=1
            self.valores[self.final] = valor
        
    
vetor = Fila(8)

for i in range(9):
    vetor.enfileirar(2*i)

vetor.imprime()