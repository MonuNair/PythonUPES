#program to find the sum of digits of a number

n=int(input("Enter the number:"))
sum=0
while n>0:
    sum+=n%10
    n=n//10
print("The sum of the digits of the number is",sum)
