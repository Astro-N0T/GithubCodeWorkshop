class Celsius:
    def __init__(self, valor=0):
        self.temperatura = valor

    def get_fahrenheit(self):
        return (self.temperatura * 1.8) + 32

    def get_kelvin(self):
        return self.temperatura + 273.15


if __name__ == "__main__":
    temperatura_celsius = Celsius(25)
    print(f"Temperatura em Celsius: {temperatura_celsius.temperatura}°C")
    temperatura_celsius.temperatura = 30
    print(f"Temperatura atualizada em Celsius: {temperatura_celsius.temperatura}°C")
    fahrenheit = temperatura_celsius.get_fahrenheit()
    print(f"Temperatura em Fahrenheit: {fahrenheit}°F")
    kelvin = temperatura_celsius.get_kelvin()
    print(f"Temperatura em Kelvin: {kelvin}K")