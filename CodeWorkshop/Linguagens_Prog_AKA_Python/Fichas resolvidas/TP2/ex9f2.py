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

    @classmethod
    def soma(cls, lista):
        total = cls(0)
        for t in lista:
            total.temperatura += t.temperatura
        return total

    @classmethod
    def media(cls, lista):
        total = cls.soma(lista)
        total.temperatura /= len(lista)
        return total


# exemplo
temp1 = Celsius(25)
temp2 = Celsius(30)
temp3 = Celsius(35)

lista_temperaturas = [temp1, temp2, temp3]

soma_temperaturas = Celsius.soma(lista_temperaturas)
print(f"Soma das temperaturas: {soma_temperaturas.temperatura} °C")  # Mostra a soma

media_temperaturas = Celsius.media(lista_temperaturas)
print(f"Média das temperaturas: {media_temperaturas.temperatura} °C")  # Mostra a média
