from dataclasses import dataclass

@dataclass
class Categoria:
    nome: str

@dataclass
class Transacao:
    descricao: str
    valor: float
    categoria: Categoria

    def exibir(self):
        print(f'DESCRICAO: {self.descricao} / VALOR: {self.valor} / CATEGORIA: {self.categoria.nome}')

# Lists to store categories and transactions
LISTA_CATEGORIAS = []
LISTA_TRANSAÇÕES = []

def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome=nome)
    LISTA_CATEGORIAS.append(nova_categoria)
    return nova_categoria

def cadastrar_transacao(descricao, valor, categoria):
    nova_transacao = Transacao(
        descricao=descricao,
        valor=valor,
        categoria=categoria
    )
    LISTA_TRANSAÇÕES.append(nova_transacao)  # Add transaction to the list
    return nova_transacao

def saldo_total():
    total = 0
    for t in LISTA_TRANSAÇÕES:
        total += t.valor
    return total

# Creating categories
categoria_receita = cadastrar_categoria('Receitas')
categoria_contas = cadastrar_categoria('Contas Fixas')
categoria_lazer = cadastrar_categoria('Lazer')
categoria_viagens = cadastrar_categoria('Viagens')

# Creating transactions
cadastrar_transacao(descricao="mesada mae", valor=50, categoria=categoria_receita)
cadastrar_transacao(descricao="Ingresso show", valor=150, categoria=categoria_lazer)
cadastrar_transacao(descricao="Conta de luz", valor=200, categoria=categoria_contas)
cadastrar_transacao(descricao="Disney", valor=20000, categoria=categoria_viagens)

# Calculating total balance
total = saldo_total()
print('Saldo total:', total)
