# Author --> Deep Gupta
Value = input("Enter the String Which is Palindrome:")

if Value == str(Value)[::-1]:
    print("This is Palindrome")
    print("", str(Value), "is Palindrome of", Value )
else:
    print("This is not Palindrome")
    print("", str(Value), "is not Palindrome of", Value)