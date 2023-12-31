class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self):
        self.annual_salary += 5000
        annual_raise = input("Raise is $5,000 but if different add amount or press q to skip: ")
        if annual_raise != 'q':
            self.annual_salary += annual_raise