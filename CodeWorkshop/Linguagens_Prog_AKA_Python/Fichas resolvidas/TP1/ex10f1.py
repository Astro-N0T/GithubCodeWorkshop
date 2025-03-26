# 10. Adicione um método que devolva o nome em MAIÚSCULAS.

class PizzaMedia():
diametro_cm=30  # O diâmetro de uma Pizza Média em centímetros

def __init__(self, nome): # Atributo da instância
self.nome = nome  # O nome da pizza, definido ao criar uma nova instância da classe, exemplo:

def nome_caps(self):
    return self.nome.upper() #func para devolver uppercase letters


     pizza1 = PizzaMedia ("Hawaian") 
     print(pizza1.nome) # Dá print a Hawaian como o nome da pizza 1
     print(pizza1.diametro_cm) # Dá print ao diametro da pizza 1
     print(pizza1.nome_maiusculas())  # Saída: HAWAIAN