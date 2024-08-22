def generator():
    yield 'Ola'
    yield 'Mundo'

result = generator()
print(next(result))  # Imprime 'Ola'
print(next(result))  # Imprime 'Mundo'