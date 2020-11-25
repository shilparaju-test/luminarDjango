# num=int(input("enter number"))
# fact=1
# if num==0:
#     print("factorial is 1")
# else:
#     for i in range(1,num):
#         fact=fact*i
#     print("factorail is ",fact)

    #with function
def fact(num):
    fact=1
    for i in range(1,(num+1)):
        fact=fact*i
    return fact
print(fact(5))
