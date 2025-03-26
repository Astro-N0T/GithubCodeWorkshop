#override ao str? se definir em classe ele retorna string?

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def getNome(self):
        return self.nome + " " + self.sobrenome

    def __str__(self):
        return self.getNome()

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, mecanografico):
        super().__init__(nome, sobrenome)
        self.mecanografico = mecanografico

    def getAluno(self):
        return self.getNome() + ", " + str(self.mecanografico)

    def __str__(self):
        return self.getAluno()

#Exemplo
aluno = Aluno("João", "Silva", 1234)
print(aluno)  #João Silva, 1234
