class TextHelper:
    def __init__(self, message):
        self.message = message

    def display_uppercase(self):
        print("Message:", self.message.upper())


class Session:
    def __init__(self, owner):
        self.owner = owner
        print(f"{owner}'s helper session started.")

    def __del__(self):
        print(f"{self.owner}'s helper session ended.")


class PairFinder:
    def find_pair(self, numbers, target):
        seen = {}
        for index, value in enumerate(numbers):
            complement = target - value
            if complement in seen:
                return seen[complement], index
            seen[value] = index
        return None


TextHelper(input("Enter a reminder: ")).display_uppercase()
session = Session("Student")
numbers = (10, 20, 30, 40, 50, 60, 70)
target = int(input("Enter a target sum: "))
pair = PairFinder().find_pair(numbers, target)
print(f"Matching positions: {pair}" if pair else "No matching pair found.")
del session
