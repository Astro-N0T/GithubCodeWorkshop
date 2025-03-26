class Agenda:
    def __init__(self):
        self.__eventos = []  # Lista privada para armazenar eventos

    def listar_eventos(self):
        """Retorna a lista de eventos armazenados."""
        return self.__eventos

    def add_evento(self, evento):
        """Adiciona um evento à lista."""
        self.__eventos.append(evento)

    def itera_eventos_cronologicamente(self):
        """
        Retorna um gerador que itera sobre os eventos da lista, ordenados cronologicamente.
        """
        eventos_ordenados = sorted(
            self.__eventos, key=lambda e: (e.data.ano, e.data.mes, e.data.dia)
        )
        for evento in eventos_ordenados:
            yield evento
