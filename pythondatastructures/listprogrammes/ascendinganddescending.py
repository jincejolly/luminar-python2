lst=[9,5,8,2,7,9,6,5,7,31]
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]<lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)

