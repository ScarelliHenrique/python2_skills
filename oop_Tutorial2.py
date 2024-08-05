class Employee:

    raise_amount=1.04 #aumento
    num_of_emps=0 #variavel de quantidade de empregados

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1#conta quantos empregados tem
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay =int(self.pay*self.raise_amount)

print(Employee.num_of_emps)#aqui vai ter 0


emp_1 = Employee('Corey', 'Taylor', 50000)
emp_2 = Employee('Test', 'User', 6000)

print(Employee.num_of_emps)#aqui vai ter 2
