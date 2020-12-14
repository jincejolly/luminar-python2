num=int(input("enter the number"))
sum=0
while(num!=0):
    data=num%10
    sum=sum+(data**3)
    num=num//10
print(sum)