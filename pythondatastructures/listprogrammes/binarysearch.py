lst=[7,2,3,6,8,1,10]
lst.sort()
element=int(input("enter the element you want to search"))
low=0
flag=0
up=len(lst)-1
while(low<=up):
    mid=(low+up)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")
