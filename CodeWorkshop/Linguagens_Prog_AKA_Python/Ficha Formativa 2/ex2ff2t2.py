from ex1ff2 import Data
from abc import ABC, abstractmethod

class EventoAbstrato(ABC):
    
    def __init__(self, name:str, data, duration):
        self.__name = name
        self.data = data
        self.duration = duration
        if duration < 1:
            raise ValueError("Invalid duration value")
        self.duration = f"{duration} dia" if duration == 1 else f"{duration} dias" 
        
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self,name):
        self.__name = name   
        
    @abstractmethod
    def duration_in_days () :
        pass
    
    def __str__(self):
        return f'{self.name}|{self.dia}/{self.mes}/{self.ano}|{self.duration}'
    
    