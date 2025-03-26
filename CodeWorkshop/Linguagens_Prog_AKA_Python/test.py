class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def getNome (self):
        return self.nome + " " + self.sobrenome

class Aluno (Pessoa):
    def __init__ (self, nome, sobrenome, num_mec):
        super().__init__(nome,sobrenome)
        self._num_mec=num_mec
        
    def __str__ (self):
        return "Dados do Aluno: " + self.nome + " " + self.sobrenome + " " + str(self._num_mec)
    
    
teste = Aluno("Adriano","Neto",123)  
print(teste)

