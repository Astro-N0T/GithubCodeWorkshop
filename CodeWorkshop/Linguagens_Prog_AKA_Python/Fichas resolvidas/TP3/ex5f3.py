class VaiAoForno:
    def getMinutosDeCozedura(self):
        #o programa acaba se e a subclasse não implementar este método
        print("Erro: Este método deve ser implementado nas subclasses.")
        exit(1)

class Pizza(VaiAoForno):
    def __init__(self, tempo):
        self.tempo = tempo
    
    def getMinutosDeCozedura(self):
        return self.tempo

class Broa(VaiAoForno):
    def __init__(self, tempo):
        self.tempo = tempo

    def getMinutosDeCozedura(self):
        return self.tempo

def cozinha_no_forno(item):
    tempo_de_cozedura = item.getMinutosDeCozedura()
    print("O forno está a cozinhar durante", tempo_de_cozedura, "minutos.")

#Exemplo
pizza = Pizza(15)
broa = Broa(30)

cozinha_no_forno(pizza)  #15 minutos
cozinha_no_forno(broa)   #30 minutos
