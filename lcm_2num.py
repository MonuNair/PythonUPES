import math

# Input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Store original values for later use
x, y = a, b  

# GCD calculation
while y:
    a, y = y, a % y  # Keep reducing

gcd = a  # Final 'a' is the GCD

lcm = math.sqrt(x * b)**2 // gcd  # LCM formula: LCM(a, b) = |a*b| / GCD(a, b)
lcm=int(lcm)

# Result
print("The LCM of", x, "and", b, "is", lcm)
