# Activity 2: Find Common Fruits

class_a = {"Apple", "Mango", "Banana"}
class_b = {"Banana", "Orange", "Apple"}

common = class_a & class_b
only_a = class_a - class_b

print("Class A:", class_a)
print("Class B:", class_b)
print("Common fruits:", common)
print("Fruits only in Class A:", only_a)
