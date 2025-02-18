a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a>b:
    add=a+b
    sub=a-b
    div=a/b
    mul=a*b
    print("The sum of the numbers is",add)
    print("The difference of the numbers is",sub)
    print("The product of the numbers is",mul)
    print("The quotient of the numbers is",div)
    
else:
    add=a+b
    sub=b-a
    div=b/a
    mul=a*b
    print("The sum of the numbers is",add)
    print("The difference of the numbers is",sub)
    print("The product of the numbers is",mul)
    print("The quotient of the numbers is",div)