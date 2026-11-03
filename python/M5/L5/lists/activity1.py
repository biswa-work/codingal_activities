from abc import ABC, abstractmethod


class BaseClass(ABC):
    def display(self, value):
        print("Value:", value)

    @abstractmethod
    def show_message(self):
        pass


class DerivedClass(BaseClass):
    def show_message(self):
        print("The abstract method is implemented in the subclass.")


obj = DerivedClass()
obj.display(25)
obj.show_message()
