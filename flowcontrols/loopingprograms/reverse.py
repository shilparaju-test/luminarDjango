num = int(input("enter num"))
res=0
while(num!=0):
    d=num%10
    res=res*10+d
    num=num//10
print(res)