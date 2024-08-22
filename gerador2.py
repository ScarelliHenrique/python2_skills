def gen(n):
    for i in range(n):
        yield i**2
import sys
x = [i**2 for i in range(100_000)]
g = gen(100_000)
print(sys.getsizeof(x)) # 824472
print(sys.getsizeof(g)) # 128
#O gerador g é mais eficiente em termos de memória porque não armazena todos os valores ao mesmo tempo, diferente da lista x.