destination = "Bangalore"
ticket_price = 750.0
tickets = 3
confirmed = True

total_cost = ticket_price * tickets
affordable = total_cost <= 3000

print(destination)
print("Total Cost:", total_cost)
print("Affordable:", affordable)

price1 = 750
price2 = 900

temp = price1
price1 = price2
price2 = temp

print(price1, price2)
