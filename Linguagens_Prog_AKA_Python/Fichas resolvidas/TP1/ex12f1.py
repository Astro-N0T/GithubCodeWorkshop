# 12. Adicione um atributo que inclua os ingredientes da pizza sob a forma de uma
# lista com str. Não esquecer da inicialização

    def __init__(self, nome, ingredientes):
        self.nome = nome  # Atributo de instância para o nome da pizza
        self.ingredientes = ingredientes  # Atributo de instância para os ingredientes da pizza

        class PizzaMedia():
        diametro_cm=30  # O diâmetro de uma Pizza Média em centímetros

        def __init__(self, nome, ingredientes): # atributos da instância
        self.nome = nome  # O nome da pizza, definido ao criar uma nova instância da classe, exemplo:
        self.ingredientes = ingredientes # ingredientes da class pizza

def nome_caps(self):
    return self.nome.upper() #func para devolver uppercase letters


# Criando a pizza Havaiana
pizza_havaiana = PizzaMedia("Havaiana", ["molho de tomate", "queijo", "presunto", "abacaxi"])

# Exibindo as informações da pizza Havaiana
print(f"Pizza: {pizza_havaiana.nome}, Ingredientes: {', '.join(pizza_havaiana.ingredientes)}")  
# Saída: Pizza: Havaiana, Ingredientes: molho de tomate, queijo, presunto, abacaxi

# Exibindo o nome da pizza em maiúsculas
print(pizza_havaiana.nome_maiusculas())  # Printa HAVAIANA
e