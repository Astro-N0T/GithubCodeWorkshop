class Ingrediente:
    """Classe para representar um ingrediente."""
    
    def __init__(self, nome, quantidade):
        self.nome = nome 
        self.quantidade = quantidade  


class PizzaMedia:
    diametro_cm = 30 
    pi = 3.14159  



    def __init__(self, nome, ingredientes=None): 
        self.nome = nome 
        if ingredientes is None:
            #se nao forem fornecidos ingredientes, usamos os ingr. padrao
            self.ingredientes = [
                Ingrediente("molho de tomate", 100), 
                Ingrediente("queijo mozarella", 150)
            ]
        else:
            self.ingredientes = ingredientes 




    def nome_maiusculas(self):
        """Retorna o nome da pizza em maiúsculas."""
        return self.nome.upper()  # Função para devolver letras maiúsculas

    def area(self):
        """Calcula e retorna a área da pizza em cm²."""
        raio_cm = self.diametro_cm / 2  
        return self.pi * (raio_cm ** 2) 


#exemplos de ingredientes
ingredientes_havaiana = [
    Ingrediente("molho de tomate", 100),
    Ingrediente("queijo", 150),
    Ingrediente("presunto", 100),
    Ingrediente("abacaxi", 80)
]


pizza_havaiana = PizzaMedia("Havaiana", ingredientes_havaiana)

ingredientes_str = ', '.join(f"{ingrediente.quantidade}g de {ingrediente.nome}" for ingrediente in pizza_havaiana.ingredientes)
print(f"Pizza: {pizza_havaiana.nome}, Ingredientes: {ingredientes_str}")

print(f"A área da pizza é: {pizza_havaiana.area():.2f} cm²")  