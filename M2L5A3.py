#diamond pattern
rows = int(input("Enter the number of rows: "))
# Upper part of the diamond
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
# Lower part of the diamond
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))