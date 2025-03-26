import datetime

class Data:
    def __init__(self, dia:int, mes:int, ano:int):
        if not Data.__Verification(dia, mes, ano):
            raise ValueError("Data invalida")
        self.dia = dia
        self.mes = mes
        self.ano = ano
        
        
    def getDiffDias(self, other):
        #Calcula a diferença de dias entre as datas self e other
        diff = datetime.datetime(self.ano, self.mes, self.dia)\
        - datetime.datetime(other.ano, other.mes, other.dia)
        return diff.days
    #Nota: a '\' permite quebrar uma linha em duas, mantendo a indentação.
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'
    
    def __Verification(dia,mes,ano):
        if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0 :
            return True
        else : 
            return False
        
    @staticmethod
    def tirarString(hoje):
        dia, mes, ano = map(int, hoje.split("/"))
        return Data(dia, mes, ano)
    
hoje = Data(19,12,2024)
haUmAno = Data(19,12,2023)
diffDiasTeste = hoje.getDiffDias(haUmAno)
print (diffDiasTeste)
print(hoje)
testint = Data.tirarString(str(hoje))
print (testint)