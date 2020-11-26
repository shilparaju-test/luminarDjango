ilst=[9,8,7,6,4,3,2]
olst=[]
for num in ilst:
    if(num>5):
        olst.append((num+1))
    elif(num<5):
        olst.append((num-1))
    elif(num==5):
        olst.append(num)
print(olst)