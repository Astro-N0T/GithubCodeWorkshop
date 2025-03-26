from num2words import num2words

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

    def extenso(self):
        valor_extenso = num2words(int(self.temperatura), lang='pt')
        grau_string = self.__get_grau_string()
        return f"{valor_extenso} {grau_string} Celsius"

    def __get_grau_string(self):
        if self.temperatura == 1 or self.temperatura == -1:
            return "grau"
        else:
            return "graus"


# Exemplo de uso
temp1 = Celsius(-1)
print(temp1.extenso())  # Mostra: "Menos um grau Celsius"

temp2 = Celsius(0)
print(temp2.extenso())  # Mostra: "Zero graus Celsius"

temp3 = Celsius(1)
print(temp3.extenso())  # Mostra: "Um grau Celsius"

temp4 = Celsius(2)
print(temp4.extenso())  # Mostra: "Dois graus Celsius"
