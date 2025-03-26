# 1. Considere a seguinte classe que define um objeto que encapsula uma data:
import datetime

class Data:
    #Define uma data com dia, mês e ano
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
            
    def getDiffDias(self, other):
        #Calcula a diferença de dias entre as datas self e other
        diff = datetime.datetime(self.ano, self.mes, self.dia)\
        - datetime.datetime(other.ano, other.mes, other.dia)
        return diff.days
    #Nota: a '\' permite quebrar uma linha em duas, mantendo a indentação.
    
    def __verify(dia, mes, ano):
        if 1 <= dia <= 31 and 1 < mes < 12 and ano > 0 :
            return True
        else : 
            return False
        
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"
    
    @staticmethod
    def from_string(hoje):
        dia, mes, ano = map(int, hoje.split("/"))
        return Data(dia, mes , ano)
        

# a) Instancie dois objetos Data em duas variáveis hoje e haUmAno, respetivamente com as
# datas de hoje e de há um ano.

hoje = Data(16,12,2024)
haUmAno = Data(16,12,2023)

# b) Imprima no ecrã quantos dias passaram desde haUmAno até hoje.
print (hoje.getDiffDias(haUmAno))


strhoje = str(hoje)
print(strhoje)


dataInt = Data.from_string(strhoje)
print (dataInt)
# c) Crie um método privado que faça uma pre-validação da data inserida (devolve
# True/False). Para simplificar, garanta apenas que o dia está no intervalo [1, 31], o mês
# [1, 12] e o ano positivo (d.c.).

# d) Faça o override ao método __str__ de forma a poder imprimir corretamente a data. Por
# exemplo: print(str( hoje )) deverá imprimir “26/1/2020”.

# e) Crie um método estático onde se passe um argumento com uma str no formato
# “26/1/2020” e que devolva um objeto do tipo Data com a respetiva data.

