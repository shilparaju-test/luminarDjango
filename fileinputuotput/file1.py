f=open("text","r")
lst=[]
for lines in f:
    lst.append(lines)
print(set(lst))

#avoid duplicates
