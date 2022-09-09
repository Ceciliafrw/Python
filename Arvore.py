class Noh:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
    
    def mostra_chave(self):
        print(self.chave)

    def mostra_esquerda(self):
        print(self.esquerda)

    def mostra_direita(self):
        print(self.direita)

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None
        self.ligacoes = []
    
    def insere(self, chave):
        novo = Noh(chave)
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz

            while True:
                if novo.chave > atual.chave:
                    if atual.direita == None:
                        atual.direita = novo
                        self.ligacoes.append(f"{atual.chave} -> {novo.chave}")
                        return
                    atual = atual.direita
            
                else:
                    if atual.esquerda == None:
                        atual.esquerda = novo
                        self.ligacoes.append(f"{atual.chave} -> {novo.chave}")
                        return
                    atual = atual.esquerda

    def busca(self, chave):
        atual = self.raiz
        pai = None
        while atual.chave != chave:
            if atual.chave > chave:
                if atual.esquerda != None:
                    pai = atual
                    atual = atual.esquerda
                else:
                    print("item não encontrado")
                    return None, None

            else:
                if atual.direita != None:
                    pai = atual
                    atual = atual.direita
                else:
                    print("item não encontrado")
                    return None, None

        return atual, pai

    def exclui(self, chave):
        excluido, pai = self.busca(chave)
        if excluido == None:
            return
        else:
            if excluido.esquerda == None and excluido.direita == None:
                if excluido.chave < pai.chave:
                    pai.esquerda = None
                else:
                    pai.direita = None

            
    
    def imprime(self):
        for i in self.ligacoes:
            print(i)
                
dados = [53,30,72,14,39,9,23,34,49,61,84,79]
arvore = ArvoreBuscaBinaria()

for dado in dados:
    arvore.insere(dado)

arvore.imprime()
print("--------------------------------")
arvore.busca(39)
arvore.busca(76)
arvore.exclui(9)
print("--------------------------------")
arvore.imprime()
arvore.busca(9)
