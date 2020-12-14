low=(int(input("enter the lower limit")))
up=(int(input("enter the upper limit")))
odd=0
even=0
for i in range(low,up):
    if(i%2==0):
        even=even+i
    else:
        odd=odd+i
print(even,odd)