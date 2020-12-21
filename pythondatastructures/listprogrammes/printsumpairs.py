lst=[2,1,3,4,6,7]
lst.sort()
element=int(input("enter the element you need to search:"))
#123467
low=0
upp=len(lst)-1
while(low<=upp):
    total=lst[low]+lst[upp]
    if(element<total):
        upp=upp-1
    if(element>total):
        low=low+1
    if(element==total):
        print("pairs are",lst[low],",",lst[upp])
        break
