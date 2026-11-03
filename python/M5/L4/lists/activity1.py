class myClass:
    __privateVar = 27

    def __privMeth(self):
        print("This is a private method.")

    def hello(self):
        print("Private value:", self.__privateVar)
        self.__privMeth()


foo = myClass()
foo.hello()

try:
    print(foo.__privateVar)
except AttributeError:
    print("Private variable cannot be accessed by that name outside the class.")

try:
    foo.__privMeth()
except AttributeError:
    print("Private method cannot be called by that name outside the class.")
