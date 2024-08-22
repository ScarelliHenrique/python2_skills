#Podemos definir um gerador que irá gerar uma sequência infinita:


def sequencia_infinita():
    num = 0
    while True:
        yield num
        num +=1
for i in sequencia_infinita():
    print(i,end=' ')
