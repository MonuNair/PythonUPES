a=0
b=1
n=int(input("Enter the number of terms:"))
for i in range(1, n):
    c=a+b
    print("c=",a+b)
    b=c
    a=b
    
    