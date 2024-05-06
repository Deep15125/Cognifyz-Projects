import random

lower = int(input("Enter the Lower Bound:"))
upper = int(input("Enter the Upper Bound:"))

value = random.randint(lower, upper)

print("The Lower Bound:", lower)
print("The Upper Bound:", upper)

Guess = int(input("Enter Your Guess:"))

while Guess != value:
    if Guess < value:
        print("Your Guess is too Low")
        Guess = int(input("Pleasee re-enter the Guess:"))
    elif Guess > value:
        print("Your Guess is too High")
        Guess = int(input("Please re-enter the Guess:"))
    else:
        break
print("Congratulations ! Your Guess is Right")
