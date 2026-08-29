#age counter(error handling)
try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("Please enter a valid age")
    else:
        years_remaining = 100 - age
except ValueError:
    print("Invalid input! Please enter a valid integer.")
else:
    print(f"You have {years_remaining} years remaining until you turn 100.")