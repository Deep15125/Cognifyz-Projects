def fibonacci_series(n):

    if n <= 1:
        return n
    else:
        return(fibonacci_series(n-1) + fibonacci_series(n-2))

nterms = int(input("Enter the Number to continue the Fabonacci Series:"))

if nterms <= 0:
    print("Pleaseeee enter the Positive Number")
else:
    print("fibonacci_series:")
    for i in range(nterms):
        print(fibonacci_series(i))