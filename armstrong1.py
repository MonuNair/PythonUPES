#program to check if the given number is an armstrong number or not

n=int(input("Enter the number:"))
sum=0
temp=n
while n>0:
    r=n%10
    sum+=r**3
    n=n//10
if temp==sum:
    print(temp,"is an armstrong number")
else:
    print(temp,"is not an armstrong number")
