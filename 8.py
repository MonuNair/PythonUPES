a=float(input("Enter your marks: "))
b=input("Have you submitted the project? (Y/N): ")
if a>60 and b=="Y":
    print("You have passed the exam and recieved C grade")
elif a>70 and b=="Y":
    print("You have passed the exam and recieved B grade")
elif a>80 and b=="Y":
    print("You have passed the exam and recieved A grade")
elif a>90 and b=="Y":
    print("You have passed the exam and recieved A+ grade")
elif a<60 and b=="Y":
    print("You have failed the exam")
elif a>60 and b=="N":
    print("You have failed the exam")
elif a>70 and b=="N":
    print("You have passed the exam and recieved C grade")
elif a>80 and b=="N":
    print("You have passed the exam and recieved B grade")
elif a>90 and b=="N":
    print("You have passed the exam and recieved A grade")
