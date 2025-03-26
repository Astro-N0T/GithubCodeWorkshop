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


# Testes
c = Celsius(25)

# Tentar acessar a propriedade 'temperatura'
print(c.temperatura)  # Mostra: 25

# Tentar acessar o atributo privado '__temperatura'
try:
    print(c.__temperatura)  # Levanta AttributeError
except AttributeError as e:
    print(e)

# Consultar o campo __dict__ do objeto
print(c.__dict__)  # Mostra: {'_Celsius__temperatura': 25}
