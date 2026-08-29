#armstrong number
num = int(input("Enter a number: "))
# calculate the number of digits
num_digits = len(str(num))
# calculate the sum of the cubes of each digit
sum_of_cubes = sum(int(digit) ** 3 for digit in str(num))
# check if the number is an Armstrong number
if num == sum_of_cubes:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")