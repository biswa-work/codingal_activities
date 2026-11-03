# Activity 3: Fruit Counter Using an Array

from array import array

fruit_counts = array("i", [4, 2, 6, 3, 5])

print("Original counts:", fruit_counts.tolist())

fruit_counts.append(7)
print("After adding a count:", fruit_counts.tolist())

print("Number of entries:", len(fruit_counts))
print("Total fruits:", sum(fruit_counts))

fruit_counts.reverse()
print("Reversed counts:", fruit_counts.tolist())
