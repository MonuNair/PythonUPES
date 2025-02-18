x=1
while(x<10):
    print("hi x",x)
    x=x+1
    
x = 1
while x < 10:
    print("hi x", x, sep="")  # No space between "hi x" and x
    x = x + 1


x = 1
while x < 10:
    print("hi x" + str(x))  # Concatenation to remove space
    x = x + 1
