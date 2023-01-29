#3.programme to calculate the factorial of a number(a non nrgative integer).the function accepts the number as an argument


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("enter a number:"))
print(factorial(n))