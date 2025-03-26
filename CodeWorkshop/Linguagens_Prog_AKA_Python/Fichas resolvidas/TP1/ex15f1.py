# 15. Desenvolva uma classe Ingrediente que inclua o nome e a quantidade (gramas) desse ingrediente.
# Altere a classe PizzaMedia de forma a receber os ingredientes sob a forma de Ingrediente (em vez de uma string).

class Ingrediente:
    """Classe para representar um ingrediente."""
    
    def __init__(self, nome, quantidade):
        self.nome = nome  # O nome do ingrediente
        self.quantidade = quantidade  # A quantidade do ingrediente em gramas

class PizzaMedia:
    diametro_cm = 30  # O diâmetro de uma Pizza Média em centímetros
    pi = 3.14159  # Aproximação de π

    def __init__(self, nome, ingredientes=None):  # Atributos da instância
        self.nome = nome  # O nome da pizza, definido ao criar uma nova instância da classe
        # Se ingredientes não forem fornecidos, usa a lista padrão
        if ingredientes is None:
            # Usando ingredientes padrão como instâncias da classe Ingrediente
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
        raio_cm = self.diametro_cm / 2  # Calculando o raio
        return self.pi * (raio_cm ** 2)  # Retornando a área usando a fórmula da área do círculo


# Criando ingredientes para a pizza Havaiana
ingredientes_havaiana = [
    Ingrediente("molho de tomate", 100),
    Ingrediente("queijo", 150),
    Ingrediente("presunto", 100),
    Ingrediente("abacaxi", 80)
]

# Criando a pizza Havaiana com ingredientes específicos
pizza_havaiana = PizzaMedia("Havaiana", ingredientes_havaiana)

# Exibindo as informações da pizza Havaiana
ingredientes_str = ', '.join(f"{ingrediente.quantidade}g de {ingrediente.nome}" for ingrediente in pizza_havaiana.ingredientes)
print(f"Pizza: {pizza_havaiana.nome}, Ingredientes: {ingredientes_str}")
# Saída: Pizza: Havaiana, Ingredientes: 100g de molho de tomate, 150g de queijo, 100g de presunto, 80g de abacaxi

# Exibindo a área da pizza Havaiana
print(f"A área da pizza é: {pizza_havaiana.area():.2f} cm²")  # Exibindo a área formatada com duas casas decimais
