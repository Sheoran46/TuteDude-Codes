def factorial(n):
    if(n==0 or n==1):
        return 1
    fact=n*factorial(n-1)
    return fact
n=int(input("enetr the number: "))
print("the factorial of n is:",factorial(n))