#4!=4X3X2X1

def factorial(n):

    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return (n*factorial(n-1))
n=-1
print(factorial(n))

# def factorial(n):
#     return 1 if (n==1 or n==0) else n*factorial(n-1)
# n=5
# print(f"factorial of {n} is {factorial(n)}")
