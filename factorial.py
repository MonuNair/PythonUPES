import math
a = float(input("Enter the number: "))

if not a<0:
    print("Invalid input. Please enter a non-negative integer.")
elif a == int(a):

    if a == 0 or a == 1:
        print("The factorial of",a,"is 1.")
    else:
        fact = 1
        for i in range(1, a + 1):
            fact *= i
        print("The factorial of",a,"is",fact)
        
else:
    a = float(a)
    b = math.gamma(a)
    print("The factorial of ",a,"is",b)