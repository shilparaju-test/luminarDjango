from functools import *

lst=[10,11,12,13,14,15]
sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)

#sum of even numbers
evensum=reduce(lambda no1,no2:no1+no2,list(filter(lambda no:no%2==0,lst)))
print(evensum)

#minimum of even  numbers

evenmin=reduce(lambda no1,no2:no1 if no1<no2 else no2,list(filter(lambda no:no%2==0,lst)))
print(evenmin)