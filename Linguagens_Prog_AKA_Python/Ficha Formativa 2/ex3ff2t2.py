from ex1ff2 import Data
from ex2ff2 import EventoAbstrato

class Evento_de_1_Dia(EventoAbstrato):
    def __init__(self):
        super().__init__(None, None, 1)  # Inicializa o evento com duração de 1 dia

    def duration_in_days(self):
        return 1  # Retorna diretamente o número de dias como inteiro

class Evento_de_2_Dias(EventoAbstrato):
    def __init__(self):
        super().__init__(None, None, 2)  # Inicializa o evento com duração de 2 dias

    def duration_in_days(self):
        return 2  # Retorna diretamente o número de dias como inteiro

def listaEventos(eventos):
    soma = 0
    for i in eventos:
        soma += i.duration_in_days()  # Soma as durações em dias
    media = soma / len(eventos) if eventos else 0  # Calcula a média
    return media

# Teste
data = Data(15, 5, 2023)  # Supondo que Data seja uma classe válida definida no ex1ff2
evento1 = Evento_de_1_Dia("Evento A", data)
evento2 = Evento_de_2_Dias("Evento B", data)
evento3 = Evento_de_1_Dia("Evento C", data)

eventos = [evento1, evento2, evento3]  # Lista de eventos
print(f"Média de duração: {listaEventos(eventos)} dias")

