class Employee:
    def __init__(self, name):
        self.name = name
        print(f"Employee {self.name} has entered.")

    def __del__(self):
        print(f"Employee {self.name} has left.")


def create_employee():
    employee = Employee("Aarav")
    print("Employee object is being used.")


create_employee()
print("Program End...")
