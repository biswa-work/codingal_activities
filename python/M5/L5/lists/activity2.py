from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("Humans walk and run.")


class Dog(Animal):
    def move(self):
        print("Dogs walk and run on four legs.")


for animal in [Human(), Dog()]:
    animal.move()
