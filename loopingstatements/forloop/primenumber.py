num=int(input("enter the number"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("not a prime")
else:
    print("it is prime")
