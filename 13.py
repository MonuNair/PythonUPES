a=int(input("Enter the number:"))

if a<0 or a is float:
    print("Invalid input.")
    
elif a==0 or a==1:
    print("The factorial of 0 is 1.")

else:
    fact=1
    for i in range (1,a+1):
        fact=fact*i
    
    print("The factorial of",a,"is",fact)    