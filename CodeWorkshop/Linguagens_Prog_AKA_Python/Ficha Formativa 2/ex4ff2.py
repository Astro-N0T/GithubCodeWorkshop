class EventoSobrepostoError(Exception):
    """Exceção personalizada para eventos sobrepostos."""
    pass


class Agenda:
    def __init__(self):
        self.__eventos = []  # Lista privada para armazenar os eventos

    def listar_eventos(self):
        """Retorna a lista de eventos."""
        return self.__eventos

    def add_evento(self, evento):
        """Adiciona um evento à lista, verificando sobreposição."""
        for ev in self.__eventos:
            if self.__ha_sobreposicao(ev, evento):
                raise EventoSobrepostoError(
                    f"O evento '{evento.name}' sobrepõe-se com '{ev.name}'"
                )
        self.__eventos.append(evento)

    def __ha_sobreposicao(self, evento1, evento2):
        """Verifica se dois eventos se sobrepõem."""
        # Supõe que os eventos têm atributos `data` e `duration`
        inicio1 = evento1.data
        fim1 = inicio1 + evento1.duration - 1
        inicio2 = evento2.data
        fim2 = inicio2 + evento2.duration - 1
        return max(inicio1, inicio2) <= min(fim1, fim2)


