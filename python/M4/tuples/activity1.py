# Activity 1: Tuple Operations

mixed = ("Alex", 12, 85.5, True)
numbers = (2, 4, 6, 4, 8)

print("Mixed tuple:", mixed)
print("Number tuple:", numbers)

new_tuple = numbers + (9,)
print("After adding 9:", new_tuple)
print("Occurrences of 4:", numbers.count(4))
print("First three elements:", numbers[:3])
