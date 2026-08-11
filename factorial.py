def factorial(x):
    '''This is a recursive function to find the factorial of an integer'''

    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

print(factorial.__doc__)
print("The factorial of 7",factorial(7))
print("The factorial of 22",factorial(22))
print("The factorial of 14",factorial(14))
