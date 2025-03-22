class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def getNome(self):
        return self.nome + " " + self.sobrenome

class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, mecanografico):
        super().__init__(nome, sobrenome) 
        #super para dar call ao init da classe pessoa para -
        #dar inicio ao nome e sobrenome e evita a repeticao do codigo
        self.mecanografico = mecanografico

    def getAluno(self):
        return self.getNome() + ", " + str(self.mecanografico)

#Exemplo
aluno = Aluno("João", "Silva", 12345)
print(aluno.getAluno())  #João Silva, 12345
