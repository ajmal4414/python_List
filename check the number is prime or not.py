#4.programme function takes a number as a parameter and check the number is prime or not

n=int(input("enter a number"))

def prime(n):
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")

prime(n)