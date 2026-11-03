class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling price: {self.__maxprice}")

    def setMaxPrice(self, price):
        if price > 0:
            self.__maxprice = price
        else:
            print("Price must be greater than zero.")


computer = Computer()
computer.sell()
computer.__maxprice = 1000
print("After direct assignment:")
computer.sell()
computer.setMaxPrice(1000)
print("After using the setter:")
computer.sell()
