# Python Object-Oriented Programming


class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay, phone):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first[0] + "." + last + phone[-2:] + "@company.com"
        self.phone = phone
        
        
        Employee.num_of_emps += 1

    def fullname(self):
        return  "First name: {} Last name: {} Email: {} Phone: {}".format(self.first, self.last, self.email, self.phone)
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay



emp_1 = Employee("Corey", "Schafer", 50000, "92964739")
emp_2 = Employee("Test", "User", 60000, "929647339")



print(emp_1.fullname())