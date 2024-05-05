def reverse(s):
    if len(s) == 0:
        print(s)
    else:
        print(s[-1])
        reverse(s[:-1])
def main():
    s = input("Enter a string: ")
    print("Reverse string of", s, "is:")
    reverse(s)


if __name__ == "__main__":
    main()