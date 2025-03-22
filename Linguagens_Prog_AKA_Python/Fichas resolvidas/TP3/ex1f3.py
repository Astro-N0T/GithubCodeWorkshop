def cozinha_no_forno(item):
    tempo_de_cozedura = item.getMinutosDeCozedura()
    print("O forno está a cozinhar durante", tempo_de_cozedura, "minutos.")

class Pizza:
    def getMinutosDeCozedura(self):
        return 20  # exemplo de temp

class Broa:
    def getMinutosDeCozedura(self):
        return 15  # exemplo de temp

#Exemplo
pizza = Pizza()
broa = Broa()

cozinha_no_forno(pizza)  #20 minutos
cozinha_no_forno(broa)   #15 minutos
