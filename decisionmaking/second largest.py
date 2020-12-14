num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
num3=int(input("enter the num3"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("num2 is the second largest")
    else:
        print("num3 is the second largest")
if(num2>num3)&(num2>num1):
    if(num3>num1):
        print("num3 is the second largest")
    else:
        print("num1 is the second largest")
if(num3>num1)&(num3>num2):
    if(num1>num2):
        print("num1 is the second largest")
    else:
        print("num2 is the second largest")
else:
    print("numbers are equal")
