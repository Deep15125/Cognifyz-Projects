#Author --> Deep Gupta
import re
value = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check(mail):
    if(re.fullmatch(value, mail)):
        print("It is Valid Mail")

    else:
        print("It is Invalid Mail")


if __name__ == "__main__":
    mail = input("Enter your Mail: ")
    check(mail)

    print("Thank You for Using Mail Checking Project")