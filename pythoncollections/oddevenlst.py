limit=int(input("enter limit"))
lst=[]
for i in range(1,limit+1):
    lst.append(i)
even=[]
odd=[]
for j in lst:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print(even)
print(odd)