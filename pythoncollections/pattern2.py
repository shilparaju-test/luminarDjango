lst=[5,4,3,2]
olst=[]
total=sum(lst)
for num in lst:
    print(num)
    olst.append((total-num))
print(olst)

