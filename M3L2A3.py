#factorial using arguments and function
def factorial(num):
    if num < 0:
        return "Please enter a positive number"
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result