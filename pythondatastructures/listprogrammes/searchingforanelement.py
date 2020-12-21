lst=[1,2,3,4,5,6,7,8]
element=int(input("enter the number"))
#if element in lst:
#    print("element found")
#else:
#    print("element not found")
flag=0
for num in lst:
    if(num==element):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("element found")

else:
    print("element not found")
