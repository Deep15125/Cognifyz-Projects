# Author --> Deep Gupta
import random

random_number = random.randint(1, 100)

Guess = int(input("Enter any number :"))

while random_number != Guess:
    if Guess > random_number:
        print("Your Guess is too High")
        Guess = int(input("Please Re-enter the number:"))
    elif Guess < random_number:
        print("Your Guess is too Low")
        Guess = int(input("Please Re-enter the number:"))
    else:
        break
print("Congrates! You Guess the Correct Number")