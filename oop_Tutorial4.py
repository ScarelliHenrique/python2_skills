class Employee:

    raise_amt=1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay=int(self.pay*self_amt)

class Developer(Employee):
    pass

dev_1 = Developer('Corey', 'Taylor', 50000)
dev_2 = Developer('Test', 'Employee', 6000)

print(help(Developer))