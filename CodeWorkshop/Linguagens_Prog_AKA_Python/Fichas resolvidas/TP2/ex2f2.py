class Celsius:
    def __init__(self, valor=0):
        self.temperatura = valor

    def get_fahrenheit(self):
        return (self.temperatura * 1.8) + 32

    def get_kelvin(self):
        return self.temperatura + 273.15

def soma(lista: list[Celsius]) -> Celsius:
    sum = Celsius(0) #objeto a ser criado
    for t in lista:
        sum.temperatura += t.temperatura
    return sum

def media(lista: list[Celsius]) -> Celsius:
    s = soma(lista)
    s.temperatura /= len(lista)

    return s


# exemplo
temps = [Celsius(10), Celsius(20), Celsius(30)]
average_temp = media(temps)
print(f"Média das temperaturas: {average_temp.temperatura} °C") 


