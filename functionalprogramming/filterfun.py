lst=[10,11,12,13,14]
even=list(filter(lambda n0:n0%2==0,lst))
print(even)


names=['ajay','binu','sam','neethu']
upper=list(map(lambda name:name.upper(),names))
print(upper)

anames=list(filter(lambda name:name[0]=='a',names))
print(anames)