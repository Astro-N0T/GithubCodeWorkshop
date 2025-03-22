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


# exemplo
temp = Celsius(25)
print(f"Temperatura: {temp.get_temperatura()} °C")  # Deve mostrar 25 °C
temp.set_temperatura(-300)  # Tenta definir uma temperatura inválida
print(f"Temperatura ajustada: {temp.get_temperatura()} °C")  # Deve mostrar -273.15 °C
