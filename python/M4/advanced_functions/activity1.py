# Activity 1: School Store Inventory Checker

items = ["Notebook", "Pencil", "Eraser", "School Bag", "Ruler"]
stock = [10, 0, 15, 3, 0]

inventory = dict(zip(items, stock))

available = [
    item for item, quantity in inventory.items()
    if quantity > 0
]

print("Complete inventory:", inventory)
print("Available items:", available)

item = input("Which item do you want to buy? ")

if item in inventory:
    if inventory[item] == 0:
        print("Sorry! This item is out of stock.")
    else:
        print("You can buy", item)
else:
    print("Item not found.")
