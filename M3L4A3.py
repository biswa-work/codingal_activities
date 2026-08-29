#Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye. with error handling

try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        while True:
            print("Bye")
    else:
        print("The number is not divisible by 2.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")