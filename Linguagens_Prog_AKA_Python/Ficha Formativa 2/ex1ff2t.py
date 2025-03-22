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
    
    def __verif (self):
        if 1 <= self.dia <= 31 and 1 <= self.mes <= 12 and self.ano > 0:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"
    
    @staticmethod
    def from_String(hoje):
        dia,mes,ano = map(int, hoje.split("/"))
        return Data (dia, mes, ano)
        
        
    
hoje = Data (9,9,2004)
haUmAno = Data (9, 12, 2003)
diff = hoje.getDiffDias(haUmAno)
print (diff)
print (hoje)
