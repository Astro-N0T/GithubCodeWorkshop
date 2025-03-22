# 14. Crie um método que devolva a área da pizza. Que tipo de método foi mais conveniente?
class PizzaMedia:
    diametro_cm = 30  # O diâmetro de uma Pizza Média em centímetros
    pi = 3.14159  # Aproximação de π

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

    def area(self):
        """Calcula e retorna a área da pizza em cm²."""
        raio_cm = self.diametro_cm / 2  # Calculando o raio
        return self.pi * (raio_cm ** 2)  # Retornando a área usando a fórmula da área do círculo

# Criando a pizza Havaiana sem especificar ingredientes
pizza_havaiana = PizzaMedia("Havaiana")

# Exibindo as informações da pizza Havaiana
print(f"Pizza: {pizza_havaiana.nome}, Ingredientes: {', '.join(pizza_havaiana.ingredientes)}")  
# Saída: Pizza: Havaiana, Ingredientes: molho de tomate, queijo mozarella

# Exibindo a área da pizza Havaiana
print(f"A área da pizza é: {pizza_havaiana.area():.2f} cm²")  # Exibindo a área formatada com duas casas decimais