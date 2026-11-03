# Activity 3: Number Challenge

numbers = [12, 7, 18, 5, 20, 9, 14]

even_numbers = [
    number for number in numbers if number % 2 == 0
]

odd_numbers = [
    number for number in numbers if number % 2 != 0
]

print("All numbers:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Sum:", sum(numbers))
print("Largest:", max(numbers))
print("Smallest:", min(numbers))
