# Activity 2: Flip Flop

values = (1, 2, 3, 3, 2, 1)

print("Original tuple:", values)
print("Reversed tuple:", values[::-1])

if values == values[::-1]:
    print("This tuple is a palindrome!")
else:
    print("This tuple is not a palindrome.")
