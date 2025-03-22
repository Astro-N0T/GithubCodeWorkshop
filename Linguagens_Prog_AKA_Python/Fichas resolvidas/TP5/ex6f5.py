#6. Implemente uma função geradora que devolva infinitamente a sucessão de
#valores de Fibonacci.

def fibonacci_infinito():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Teste
gerador = fibonacci_infinito()
for _ in range(10):
    print(next(gerador), end=" ")