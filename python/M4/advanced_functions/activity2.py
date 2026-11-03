# Activity 2: Price Calculator Using Functions

def calculate_total(price, quantity):
    return price * quantity

def apply_discount(total, discount=0):
    return total - (total * discount / 100)

price = 50
quantity = 3

total = calculate_total(price, quantity)
final_price = apply_discount(total, 10)

print("Original total:", total)
print("Discounted total:", final_price)
