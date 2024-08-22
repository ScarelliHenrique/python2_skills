#gerador que é capaz de calcular números fibonacci
def fib_gen(n):
    a = b = 1
    for e in range(n):
        a, b = b, a + b
        yield a
for x in fib_gen(7):
    print(x)