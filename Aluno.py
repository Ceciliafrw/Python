class Aluno:
    def __init__(self, nomeCriado, sobrenomeCriado):
        self.nome = nomeCriado
        self.sobrenome = sobrenomeCriado
        self.usuario = None
        self.senha = None
    
    def criarLogin(self, usuarioCriado, senhaCriada):
        self.usuario = usuarioCriado
        self.senha = senhaCriada

    def exibirAluno(self):
        print("Nome: %s\nSobrenome: %s\nUsuario: %s\nSenha: %s\n" %(self.nome, self.sobrenome, self.usuario, self.senha))

    def mudarUsuario(self, novoUsuario):
        self. novoUsuario  = novoUsuario
    
    def mudarSenha(self, novaSenha):
        self. novaSenha = novaSenha

nome = input("Escreva seu nome: ")
sobrenome = input("Escreva seu sobrenome: ")
usuario = input("Digite seu ID: ")
senha = input("Digite uma senha: ")

Novo = Aluno(nome, sobrenome)

Novo.criarLogin(usuario, senha)
Novo.exibirAluno()


