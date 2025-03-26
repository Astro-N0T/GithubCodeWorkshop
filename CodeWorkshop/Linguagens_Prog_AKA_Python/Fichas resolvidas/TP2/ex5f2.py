class Celsius:
    def __init__(self, valor=0):
        self.__temperatura = valor  # Atributo privado para armazenar a temperatura
        if self.__temperatura < -273.15:
            self.__temperatura = -273.15  # Garante que a temperatura não é menor que -273.15

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, valor):
        if valor < -273.15:
            print("Temperatura inválida! Definindo para -273.15 ºC.")
            self.__temperatura = -273.15
        else:
            self.__temperatura = valor

    def get_fahrenheit(self):
        return (self.get_temperatura() * 1.8) + 32

    def get_kelvin(self):
        return self.get_temperatura() + 273.15


def soma(lista: list[Celsius]) -> Celsius:
    soma_temp = Celsius(0)  # Cria um objeto Celsius para somar as temperaturas
    for c in lista:
        soma_temp.set_temperatura(soma_temp.get_temperatura() + c.get_temperatura())  # Usa o getter para aceder à temperatura
    return soma_temp


def media(lista: list[Celsius]) -> Celsius:
    if not lista:  # Verifica se a lista está vazia
        return Celsius()  # Retorna uma nova instância de Celsius com temperatura 0
    s = soma(lista)  # Usa a função soma para obter o total
    s.set_temperatura(s.get_temperatura() / len(lista))  # Calcula a média das temperaturas
    return s


# exemplo
temperaturas = [Celsius(25), Celsius(30), Celsius(-10)]
resultado_soma = soma(temperaturas)
print(f"Soma das temperaturas: {resultado_soma.get_temperatura()} °C")  # Mostra a soma das temperaturas

resultado_media = media(temperaturas)
print(f"Média das temperaturas: {resultado_media.get_temperatura()} °C")  # Mostra a média das temperaturas
