#program to check the divisibility of a number with 5 an 7

n=int(input("Enter the number:"))
if n%5==0 and n%7==0:
    print(n,"is divisible by 5 and 7")
else:
    print(n,"is not divisible by 5 and 7")
    