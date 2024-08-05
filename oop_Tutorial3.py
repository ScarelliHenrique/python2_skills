class Employee:
    
    raise_amount = 1.04  # aumento
    num_of_emps = 0  # variavel de quantidade de empregados

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1  # conta quantos empregados tem

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


from datetime import date
my_date = date(2024, 7, 19)
print(Employee.is_workday(my_date))  # True se for um dia útil, False caso contrário
