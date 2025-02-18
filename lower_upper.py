#program to convert all lower case to uppercase of given string

a=input("Enter the string:")
print(a.upper())


# Program to convert all lowercase letters to uppercase in a given string without using .upper() function

a = input("Enter the string: ")
result = ""

for char in a:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    else:
        result += char

print(result)