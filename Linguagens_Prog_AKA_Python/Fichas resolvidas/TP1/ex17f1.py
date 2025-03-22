#15. Imagina agora que além de pizzas médias também queres disponibilizar pizzas pequenas e grandes.
class Ingrediente:
    """Classe para representar um ingrediente."""
    
    def __init__(self, nome, quantidade):
        self.nome = nome  # O nome do ingrediente
        self.quantidade = quantidade  # A quantidade do ingrediente em gramas


class Pizza:
    """Classe base para representar uma pizza."""
    
    def __init__(self, nome, diametro_cm, ingredientes=None):
        self.nome = nome  # O nome da pizza
        self.diametro_cm = diametro_cm  # O diâmetro da pizza
        # Se ingredientes não forem fornecidos, usa a lista padrão
        if ingredientes is None:
            self.ingredientes = [
                Ingrediente("molho de tomate", 100), 
                Ingrediente("queijo mozarella", 150)
            ]
        else:
            self.ingredientes = ingredientes  # Ingredientes da pizza

    def nome_maiusculas(self):
        """Retorna o nome da pizza em maiúsculas."""
        return self.nome.upper()  # Função para devolver letras maiúsculas

    def area(self):
        """Calcula e retorna a área da pizza em cm²."""
        pi = 3.14159  # Aproximação de π
        raio_cm = self.diametro_cm / 2  # Calculando o raio
        return pi * (raio_cm ** 2)  # Retornando a área usando a fórmula da área do círculo


class PizzaPequena(Pizza):
    """Classe para representar uma pizza pequena."""
    
    def __init__(self, nome, ingredientes=None):
        super().__init__(nome, diametro_cm=20, ingredientes=ingredientes)  # Definindo o diâmetro como 20 cm


class PizzaMedia(Pizza):
    """Classe para representar uma pizza média."""
    
    def __init__(self, nome, ingredientes=None):
        super().__init__(nome, diametro_cm=30, ingredientes=ingredientes)  # Definindo o diâmetro como 30 cm


class PizzaGrande(Pizza):
    """Classe para representar uma pizza grande."""
    
    def __init__(self, nome, ingredientes=None):
        super().__init__(nome, diametro_cm=40, ingredientes=ingredientes)  # Definindo o diâmetro como 40 cm


# Criando ingredientes para a pizza Havaiana
ingredientes_havaiana = [
    Ingrediente("molho de tomate", 100),
    Ingrediente("queijo", 150),
    Ingrediente("presunto", 100),
    Ingrediente("abacaxi", 80)
]

# Criando a pizza Havaiana como uma Pizza Média
pizza_havaiana_media = PizzaMedia("Havaiana", ingredientes_havaiana)

# Exibindo as informações da pizza Havaiana
ingredientes_str = ', '.join(f"{ingrediente.quantidade}g de {ingrediente.nome}" for ingrediente in pizza_havaiana_media.ingredientes)
print(f"Pizza: {pizza_havaiana_media.nome}, Ingredientes: {ingredientes_str}")
# Saída: Pizza: Havaiana, Ingredientes: 100g de molho de tomate, 150g de queijo, 100g de presunto, 80g de abacaxi

# Exibindo a área da pizza Havaiana
print(f"A área da pizza média é: {pizza_havaiana_media.area():.2f} cm²")  # Exibindo a área formatada com duas casas decimais

# Criando uma pizza grande
pizza_havaiana_grande = PizzaGrande("Havaiana Grande", ingredientes_havaiana)

# Exibindo as informações da pizza Havaiana Grande
ingredientes_str_grande = ', '.join(f"{ingrediente.quantidade}g de {ingrediente.nome}" for ingrediente in pizza_havaiana_grande.ingredientes)
print(f"Pizza: {pizza_havaiana_grande.nome}, Ingredientes: {ingredientes_str_grande}")
# Saída: Pizza: Havaiana Grande, Ingredientes: 100g de molho de tomate, 150g de queijo, 100g de presunto, 80g de abacaxi

# Exibindo a área da pizza Havaiana Grande
print(f"A área da pizza grande é: {pizza_havaiana_grande.area():.2f} cm²")  # Exibindo a área formatada com duas casas decimais
# 