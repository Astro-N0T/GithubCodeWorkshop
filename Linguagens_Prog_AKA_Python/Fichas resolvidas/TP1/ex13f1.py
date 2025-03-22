# 13. Garanta que quando os ingredientes são omitidos, a pizza fica com ‘tomate’ e ‘queijo mozarella’.
class PizzaMedia:
    diametro_cm = 30  # O diâmetro de uma Pizza Média em centímetros

    def __init__(self, nome, ingredientes=None):  # Atributos da instância
        self.nome = nome  # O nome da pizza, definido ao criar uma nova instância da classe
        # Se ingredientes não forem fornecidos, usa a lista padrão
        if ingredientes is None:
            self.ingredientes = ["molho de tomate", "queijo mozarella"]  # Ingredientes padrão
        else:
            self.ingredientes = ingredientes  # Ingredientes da pizza

    def nome_maiusculas(self):
        """Retorna o nome da pizza em maiúsculas."""
        return self.nome.upper()  # Função para devolver letras maiúsculas


# Criando a pizza Havaiana
pizza_havaiana = PizzaMedia("Havaiana", ["molho de tomate", "queijo", "presunto", "abacaxi"])

# Exibindo as informações da pizza Havaiana
print(f"Pizza: {pizza_havaiana.nome}, Ingredientes: {', '.join(pizza_havaiana.ingredientes)}")  
# Saída: Pizza: Havaiana, Ingredientes: molho de tomate, queijo, presunto, abacaxi

# Exibindo o nome da pizza em maiúsculas
print(pizza_havaiana.nome_maiusculas())  # Printa HAVAIANA
