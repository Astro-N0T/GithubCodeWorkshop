class Celsius:
    def __init__(self, valor=0):
        self.__temperatura = valor
        if self.__temperatura < -273.15:
            self.__temperatura = -273.15

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor < -273.15:
            print("Temperatura inválida! Definindo para -273.15 ºC.")
            self.__temperatura = -273.15
        else:
            self.__temperatura = valor

    def get_fahrenheit(self):
        return (self.temperatura * 1.8) + 32

    def get_kelvin(self):
        return self.temperatura + 273.15


# exemplo
temp = Celsius(25)
print(f"Temperatura: {temp.temperatura} °C")  # Mostra 25 °C
temp.temperatura = -300  # Tenta definir uma temperatura inválida
print(f"Temperatura ajustada: {temp.temperatura} °C")  # Deve mostrar -273.15 °C

temp.temperatura = 30  # Define uma nova temperatura válida
print(f"Temperatura: {temp.temperatura} °C")  # Mostra 30 °C
print(f"Temperatura em Fahrenheit: {temp.get_fahrenheit()} °F")  # Mostra a temperatura em Fahrenheit
print(f"Temperatura em Kelvin: {temp.get_kelvin()} K")  # Mostra a temperatura em Kelvin
