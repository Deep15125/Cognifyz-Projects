#Author --> Deep Gupta
Celsius = float(input("Enter the Temperature in C:"))
Fahrenheit = (Celsius * 1.8) + 32

print(str(Celsius) + " degree Celsius is equal to " + str(Fahrenheit) + " degree Fahrenheit")


Fahrenheit = float(input("Enter the Temperature in F:"))
Celsius = (Fahrenheit - 32) * 5/9

print(str(Fahrenheit) + " degree Fahrenheit is equal to " + str(Celsius) + " degree Celsius")

print("Do you want to try Again ? (Y/N)")

ans = input().lower()
if ans == 'n':
    print("Thank you For using Celsius to Fahrenheit converter and Fahrenheit to Celsius Converter")    
    