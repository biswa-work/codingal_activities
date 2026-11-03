class BankAccount:
    def __init__(self, holder, pin):
        self.holder = holder
        self.__pin = str(pin)

    def set_pin(self, old_pin, new_pin):
        if self.__pin == str(old_pin) and str(new_pin).isdigit() and len(str(new_pin)) == 4:
            self.__pin = str(new_pin)
            print("PIN updated successfully.")
        else:
            print("PIN update failed.")

    def verify_pin(self, pin):
        return self.__pin == str(pin)

    def __str__(self):
        return f"Account holder: {self.holder} | PIN: ****"


account = BankAccount("Aarav", 1234)
print(account)
try:
    print(account.__pin)
except AttributeError:
    print("The PIN is private and cannot be accessed directly.")
old_pin = input("Enter current PIN: ")
new_pin = input("Enter a new four-digit PIN: ")
account.set_pin(old_pin, new_pin)
print(account)
print("New PIN verification:", account.verify_pin(new_pin))
