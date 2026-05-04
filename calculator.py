print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice=int(input("Enter 1,2,3 or 4: "))
if(choice>=1 and choice<=4):
    a=float(input("Enter 1st no.: "))
    b=float(input("Enter 2nd no.: "))
    if(choice==1):
        add=a+b
        print("a+b= ",add)
    elif(choice==2):
        sub=a-b
        print("a-b= ",sub)
    elif(choice==3):
        mul=a*b
        print("a*b= ",mul)
    elif(choice==4):
        div=a/b
        print("a/b= ",div)
else:
    print("Invalid choice")
