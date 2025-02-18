a = input("Enter the number: ")

# Check if input is a valid positive integer
if not a<0:
    print("Invalid input. Please enter a non-negative integer.")
else:
    a = int(a)

    if a == 0 or a == 1:
        print(f"The factorial of {a} is 1.")
    else:
        fact = 1
        for i in range(1, a + 1):
            fact *= i
        print(f"The factorial of {a} is {fact}.")

