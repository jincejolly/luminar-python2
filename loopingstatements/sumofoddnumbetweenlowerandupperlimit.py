low=int(input("enter the lower limit"))
up=int(input("enter the upper limit"))
sum=0
while(low<=up):
    if(low%2!=0):
        sum=sum+low
    low+=1
print(sum)
