#Encapsulamento Privado
class Calculadora:
    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__adicionar(num1, num2)# esconde o atributo
        elif op == '-':
            return self.__subtrair(num1, num2)# esconde o atributo
        else:
            print('Operação inválida')

    def __adicionar(self, num1, num2):
        return num1 + num2

    def __subtrair(self, num1, num2):
        return num1 - num2

calc = Calculadora()
resultado1 = calc.calcular('+', 5, 3)
print(resultado1)  

resultado2 = calc.calcular('-', 5, 3)
print(resultado2) 

resultado3 = calc.calcular('*', 5, 3)