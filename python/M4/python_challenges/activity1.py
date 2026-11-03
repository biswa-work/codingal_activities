# Activity 1: Shopping Challenge

shopping_cart = {
    "Notebook": 40,
    "Pencil": 10,
    "Eraser": 5,
    "Ruler": 15
}

total = 0

for item, price in shopping_cart.items():
    print(item, "- Rs.", price)
    total += price

print("Total shopping cost: Rs.", total)

if total >= 50:
    print("You qualify for a shopping reward!")
else:
    print("Add more items to qualify.")
