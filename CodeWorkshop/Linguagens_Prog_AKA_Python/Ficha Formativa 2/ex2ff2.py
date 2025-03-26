from abc import ABC, abstractmethod
#import datetime

# Classe abstrata EventoAbstrato herda de Data
class EventoAbstrato(ABC):
    def __init__(self, data, name, duration):
        self.data = data
        self.__name = name 
        self.duration = duration
        if duration == 1:
            return f'{duration} dia'
        elif duration > 1:
            return f'{duration} dias'
        else:
            return ValueError
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name

    @abstractmethod
    def duration_in_days(self):
        pass  
    
    def __str__(self):
        return f'{self.name}|{self.dia}/{self.mes}/{self.ano}|{self.duration}'
    
    #@staticmethod
    #def is_overlapped(self,other):
        #dar call ao duration_in_days
        #sacar o diff days do exercicio 1