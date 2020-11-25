max=int(input("enter max value"))
#min=int(input("enter min value"))
evensum=0
oddsum=0
num=1
while(num<=max):
    if (num%2==0):
        evensum=evensum+num
    else:
        oddsum=oddsum+num
    num+=1
print("The sum of Even numbers", evensum)
print("The sum of odd numbers", oddsum)