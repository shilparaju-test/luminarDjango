num=int(input("enter number"))
#if(num==2):
    #print("prime number")
flag=0
for i in range(2,num):
    if(num%2==0):
        flag+=1
        break
if(flag==0):
    print("prime number")
else:
    print("not prime")