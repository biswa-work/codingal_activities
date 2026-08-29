#sum of natural numbers
num = int(input("Enter a number: "))
if num < 0:
    print("Please enter a positive number")
else:
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print("The sum of natural numbers from 1 to", num, "is:", sum)