lst=[-2,-1,0,2,3,4]
cnt=1
for i in range(0,len(lst)):
    if cnt in lst:
        cnt+=1
    else:

        print(cnt,"is the least positive missing integer")
        break
