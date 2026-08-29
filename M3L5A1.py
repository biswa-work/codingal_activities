#number game (random and math module)
import random
import math

number = random.randint(1, 100)
guess = None
attempts = 0

while guess != number:
    try:
        guess = int(input("Guess the number (1-100): "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

print(f"Congratulations! You guessed the number in {attempts} attempts.")