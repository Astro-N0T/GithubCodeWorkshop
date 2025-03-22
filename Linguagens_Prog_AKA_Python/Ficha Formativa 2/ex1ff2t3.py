

import datetime

class Data:
    def __init__(self, dia, mes, ano): 
        self.dia = dia 
        self.mes = mes 
        self.ano = ano
        
    def __verif (self):
        if 1 <= self.dia <= 31 and 1 < self.mes <= 12 and self.ano > 0:
            return True
        else :
            return False
            
    def getDiffDias(self, other):
        #Calcula a diferença de dias entre as datas self e other
        diff = datetime.datetime(self.ano, self.mes, self.dia)\
        - datetime.datetime(other.ano, other.mes, other.dia)
        return diff.days
    #Nota: a '\' permite quebrar uma linha em duas, mantendo a indentação.
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'
    
    @staticmethod
    def getDias (string) :
        dia,mes,ano = map(int, string.split("/"))
        return Data(dia,mes,ano)
    
    # Object instances
hoje = Data(16,1,2025)
haUmAno = Data(16,1,2024)

diff = hoje.getDiffDias(haUmAno)
print(diff)