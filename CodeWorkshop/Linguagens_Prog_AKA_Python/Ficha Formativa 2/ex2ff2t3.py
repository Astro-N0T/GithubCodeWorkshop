from abc import ABC, abstractmethod
from ex1ff2t3.py import Data


class EventoAbstrato (ABC) :
    
    def __init__(self, data : Data, name : str ):
        self.data = data
        self.name = name
    
    @abstractmethod
    def duration_in_days (self):
        pass
    
    
    @property
    def duration (self):
        if self.data == 1 :
            return f'{self.data} dia'
        else : 
            return f'{self.data} dias'
            
    
    def __str__ (self) :
        return f'Exame|{self.data}|{self.duracao}'
        
    