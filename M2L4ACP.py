#binary conversion
number = int(input("Enter a decimal number: "))
if number < 0:
    print("Please enter a positive number")
else:
    binary = bin(number).replace("0b", "")
    print(f"The binary representation of {number} is: {binary}")