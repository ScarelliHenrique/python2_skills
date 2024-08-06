#Getters / Setters e Estados
class Pessoa:

    def __init__(self, nome:str, idade:int, )->None:
        self.nome = nome #substantivo
        self.idade = idade #substantivo

    def digirir(self,veiculo)->None: 
        print('Dirigindo um(a) {}'.format(veiculo))

    def cantar(self)->None:
        print('Lalalala')
    def apresentar_idade(self)->str:

        return self.idade
    
class Alarme:
    def __init__(self,estado:bool) -> None:
        self.__estado=estado
    def get__estado(self)->bool:
        return self.__estado
    def  set_estado(self,valor:bool)->None:
        self__estado=valor