# Author --> Deep Gupta
import re

password = input("Enter the Strong Password:")

def validate_password(password):
    if len(password) < 8:
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    if not re.search(r'[!@#$%Z^z7*(),.:[{}<>/?|]', password):
        return False
    return True

is_valid = validate_password(password)

if is_valid:
    print("Your Password is Valid")
else:
    print("Your Password is Invalid")