#SOLID (S) - Responsabilidade Única..A partir de uma retomada ao livro Clean Architecture (Bob Martin), retomamos o conceito e a definição do dado princípio e, por fim, o aplicamos em um exemplo definido
class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print('Acessando banco de dados...')
        print('Cadastrando o usuário {}, idade {}'.format(nome, idade))

    def __indicar_erro(self) -> None:
        print('Dados inválidos!')
