class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0
        
    def vendeu(self, vendas):
        self.vendas += vendas  
        
    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, 'bateu a meta')
        else:
            print(self.nome, 'Nao bateu a meta')

nome_vendedor = input('Qual o nome do vendedor?')
Vendedor1 = Vendedor(nome_vendedor)

Vendedor1.vendeu(1000)
Vendedor1.bateu_meta(600)

print(Vendedor1.vendas)
