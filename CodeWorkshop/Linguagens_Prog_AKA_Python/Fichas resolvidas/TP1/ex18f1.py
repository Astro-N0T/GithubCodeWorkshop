# 16. Documente devidamente a classe e todos os métodos
class Ingrediente:
    """
    Classe para representar um ingrediente de uma pizza.

    Atributos:
        nome (str): O nome do ingrediente.
        quantidade (float): A quantidade do ingrediente em gramas.
    """

    def __init__(self, nome, quantidade):
        """
        Inicializa um ingrediente com um nome e uma quantidade.

        Args:
            nome (str): O nome do ingrediente (ex: 'queijo mozarella').
            quantidade (float): A quantidade do ingrediente em gramas.
        """
        self.nome = nome  # O nome do ingrediente
        self.quantidade = quantidade  # A quantidade do ingrediente em gramas


class Pizza:
    """
    Classe para representar uma pizza com uma lista de ingredientes.

    Atributos:
        ingredientes (list[Ingrediente]): Lista de ingredientes da pizza. Cada ingrediente
        é uma instância da classe Ingrediente, contendo o nome e a quantidade em gramas.
    """

    def __init__(self, ingredientes=None):
        """
        Inicializa uma pizza com uma lista de ingredientes.

        Se os ingredientes não forem fornecidos, será usada uma lista padrão com
        'molho de tomate' e 'queijo mozarella'.

        Args:
            ingredientes (list[Ingrediente], opcional): Lista de objetos Ingrediente.
            Caso não seja fornecida, a pizza será inicializada com ingredientes padrão.
        """
        # Se ingredientes não forem fornecidos, usa ingredientes padrão
        if ingredientes is None:
            self.ingredientes = [
                Ingrediente("molho de tomate", 100),
                Ingrediente("queijo mozarella", 150)
            ]
        else:
            self.ingredientes = ingredientes  # Lista de ingredientes fornecida pelo usuário

    def peso_ingredientes(self):
        """
        Calcula e retorna o peso total dos ingredientes da pizza.

        O peso é a soma das quantidades de todos os ingredientes da pizza.

        Returns:
            float: O peso total dos ingredientes da pizza em gramas.
        """
        peso_total = sum(ingrediente.quantidade for ingrediente in self.ingredientes)
        return peso_total  # Retorna o peso total dos ingredientes
