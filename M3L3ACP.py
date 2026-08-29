#due amount using function and arguments and keywords and loops
def due_amount(due):
    if due < 0:
        return "Please enter a positive number"
    else:
        while due > 0:
            print(f"Due amount: {due}")
            payment = float(input("Enter payment amount: "))
            if payment <= 0:
                print("Please enter a positive payment amount.")
                continue
            due -= payment
        return "All dues are cleared!"