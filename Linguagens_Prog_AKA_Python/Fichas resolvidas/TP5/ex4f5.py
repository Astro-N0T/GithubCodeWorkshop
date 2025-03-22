#4. Considere a seguinte classe incompleta. Esta classe já é iterável porque
#implementa __iter__ que retorna um iterador. O objeto iterador é self, ou
#seja, o próprio objeto. Complete a classe de forma a implementar o iterador
#__next__() que retorne iterativamente as potências de 2 até um máximo de
#self.max elementos.


class PowTwo:
    """Classe para implementar um iterador de potências de 2"""
    
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = 2 ** self.n
        self.n += 1
        return result

print([l for l in PowTwo(10)])
