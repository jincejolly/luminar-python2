lst=[6,6,8,9,4,2,3]
out=[]
for num in lst:
    if(num>5):
        data=num+1
    else:
        data=num-1
    out.append(data)
print(out)