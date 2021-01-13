lst=[21,20,18,22,7,2,25]
lst.sort()
num=int(input("enter elememt"))
flag=0
low=0
upp=len(lst)-1
while(low<=upp):
    mid=(low+upp)//2
    if(num>lst[mid]):
        low=mid+1
    elif(num<lst[mid]):
        upp=mid-1
    elif(num==lst[mid]):
        flag+=1
        break
if(flag==0):
    print("not found")
else:
    print("found")