a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter the third number:"))
if a>b and a>c:
    if a==int(a):
        print("The largest number is",int(a))
    else:
        print("The largest number is",a)
        
elif b>a and b>c:
    if b==int(b):
        print("The largest number is",int(b))
    else:
        print("The largest number is",b)
        
elif c>a and c>b:
    if c==int(c):
        print("The largest number is",int(c))
    else: 
        print("The largest number is",c)

else:
    print("Invalid input.")
    