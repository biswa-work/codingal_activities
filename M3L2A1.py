#sum of whole numbers using function and arguments
def sum_of_whole_numbers(num):
    if num < 0:
        return "Please enter a positive number"
    else:
        sum = 0
        for i in range(1, num + 1):
            sum += i
        return sum