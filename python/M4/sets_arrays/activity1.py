# Activity 1: Class Fruit Basket Organizer

basket_one = {"Apple", "Banana", "Mango", "Orange"}
basket_two = {"Banana", "Grapes", "Mango", "Kiwi"}

print("Basket one:", basket_one)
print("Basket two:", basket_two)

shared = basket_one.intersection(basket_two)
all_fruits = basket_one.union(basket_two)

print("Shared fruits:", shared)
print("All unique fruits:", all_fruits)
