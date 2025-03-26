#5. Na sucessão de Fibonacci o elemento seguinte resulta da soma dos dois
#anteriores. Para F0=0 e F1=1, o termo Fn = Fn-1 + Fn-2.
#Desenvolva uma classe que permita a iteração dos N primeiros termos da sucessão
#de Fibonacci.

class Fibonacci:
    """Classe para iterar sobre os N primeiros termos da sucessão de Fibonacci"""
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.a, self.b = 0, 1
        self.n = 0
        return self

    def __next__(self):
        if self.n >= self.max:
            raise StopIteration
        if self.n == 0:
            self.n += 1
            return self.a
        if self.n == 1:
            self.n += 1
            return self.b
        self.a, self.b = self.b, self.a + self.b
        self.n += 1
        return self.a

print([l for l in Fibonacci(10)])
