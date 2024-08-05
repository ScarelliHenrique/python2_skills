class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf  # esconde o atributo

    def correr(self):
        print("Estou correndo")

    def beber(self, bebida):
        if bebida == "Cerveja":
            self.__apresentar_documento()
        print('Bebendo...')

    def __apresentar_documento(self):
        print(self.__cpf)

Ronaldo = Pessoa('Ronaldo', 32, "47501516897")
Ronaldo.beber('Cerveja')
Ronaldo.beber('Coca-cola')
