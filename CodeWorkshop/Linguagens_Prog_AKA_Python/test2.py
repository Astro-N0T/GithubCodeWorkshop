class Veiculo :
    
    def __init__(self, nome:str, cor: str, num_rodas: int):
        self._nome=nome
        self._cor=cor
     
    @property
    def num_rodas (self):
        self.__num_rodas = num_rodas
    
    @num_rodas.setter
    def num_rodas(self, num_rodas):
        return num_rodas
    
    def descricao (self):
        return self._nome+self._cor+str(self.num_rodas)

bicileta = Veiculo("Pasteleira","Vermelho",2)

print(bicileta.descricao())
