from pprint import pprint

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        pprint("Nguyen")

class Employee(Person):
    def print_first_name(self):
        super().print_first_name()
        print(" is an employee")

    def __init__(self, first_name, last_name, staff_id):
        super().__init__(first_name, last_name)
        self.staff_id = staff_id

if __name__ == "__main__":
    # aPerson = Person()
    # aPerson.print_first_name()
    anEmployee = Employee("Nguyen", "Duc Hoang", "12345")
    pprint(anEmployee.first_name)
    pprint(anEmployee.last_name)
    pprint(anEmployee.staff_id)
