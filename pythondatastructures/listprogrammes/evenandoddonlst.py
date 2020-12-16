limit=int(input("enter the limit"))
odd=[]
even=[]
for i in range(1,limit+1):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("odd=",odd)
print("even=",even)

