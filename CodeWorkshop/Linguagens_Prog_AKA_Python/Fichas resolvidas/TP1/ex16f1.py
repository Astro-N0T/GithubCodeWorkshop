# 16. Desenvolva um método que permita obter o peso dos ingredientes da pizza.
class Ingrediente:
    """Classe para representar um ingrediente."""
    
    def __init__(self, nome, quantidade):
        self.nome = nome  # O nome do ingrediente
        self.quantidade = quantidade  # A quantidade do ingrediente em gramas


class Pizza:
    """Classe para representar uma pizza."""

    def __init__(self, ingredientes=None):
        # Se os ingredientes não forem fornecidos, define ingredientes padrão
        if ingredientes is None:
            self.ingredientes = [
                Ingrediente("molho de tomate", 100),
                Ingrediente("queijo mozarella", 150)
            ]
        else:
            self.ingredientes = ingredientes  # Ingredientes fornecidos

    def peso_ingredientes(self):
        """Calcula e retorna o peso total dos ingredientes da pizza em gramas."""
        peso_total = sum(ingrediente.quantidade for ingrediente in self.ingredientes)
        return peso_total  # Retorna o peso total dos ingredientes


# Criando ingredientes específicos para uma pizza
ingredientes_havaiana = [
    Ingrediente("molho de tomate", 100),
    Ingrediente("queijo mozarella", 150),
    Ingrediente("presunto", 100),
    Ingrediente("abacaxi", 80)
]

# Criando uma pizza com ingredientes específicos
pizza_havaiana = Pizza(ingredientes_havaiana)

# Exibindo o peso total dos ingredientes da pizza Havaiana
print(f"O peso total dos ingredientes é: {pizza_havaiana.peso_ingredientes()}g")
# Saída: O peso total dos ingredientes é: 430g
# 