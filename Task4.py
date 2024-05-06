# Author --> Deep Gupta
Number1 = float(input("Enter the 1st Number:"))
Number2 = float(input("Enter the 2nd Number:"))

print("Choose the Operator: \n+(Add)\n-(Substract)\n*(Multiplication)\n/(Divide)\n%(Module)\n")
Operator = input("Enter the Operator:")

if Operator == "+":
    print(Number1 + Number2)
elif Operator == "-":
    print(Number1 - Number2)
elif Operator == "*":
    print(Number1 * Number2)
elif Operator == "/":
    print(Number1 / Number2)
elif Operator == "%":
    print(Number1 % Number2)

print("Thank you for calculating")