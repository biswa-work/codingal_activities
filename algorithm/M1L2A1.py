snack = "Chips"
price = 20.0
quantity = 2
available = True

total = price * quantity
affordable = total <= 100

print(snack[0])

temp = price
price = total
total = temp

print(snack, price, quantity, available, affordable)
