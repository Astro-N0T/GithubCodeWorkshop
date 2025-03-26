#nao percebi muito bem o enunciado, qual dos exercicios devia pegar como exemplo?
#vou o exercicio da soma de graus

class Celsius:
    def __init__(self, valor=0):
        self.temperatura = valor

    def __add__(self, valor2):
        if isinstance(valor2, Celsius): #verificar se é obj celsius
            return Celsius(self.temperatura + valor2.temperatura) #devolver a soma dos dois
        else:
            print("Erro: Utilize apenas temperaturas em graus celsius, que sejam somáveis entre si.")
            exit(0)  #programa acaba 
            
    def __str__(self):
        return f"{self.temperatura}°C"

#exemplo
c1 = Celsius(5)
c2 = Celsius(10)
c3 = c1 + c2  #soma direta entre os dois
print(c3)  #15°C
